from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
import json
from datetime import date


def index(request):
    invoice_form = forms.InvoiceForm(request.POST or None)
    advance_payment_form = forms.AdvancePaymentForm(request.POST or None)
    documents_form = forms.DocumentsForm(request.POST or None)
    seller_form = forms.SellerForm(request.POST or None)
    buyer_form = forms.BuyerForm(request.POST or None)
    shipper_form = forms.ShipperForm(request.POST or None)
    consignee_form = forms.ConsigneeForm(request.POST or None)
    additional_info_form = forms.AdditionalInfoForm(request.POST or None)
    section_form = forms.SectionForm(request.POST or None)
    product_form = forms.ProductForm(request.POST or None)
    info_block_form = forms.InfoBlockForm(request.POST or None)
    transfer_details_form = forms.TransferDetailsForm(request.POST or None)
    document_creator_form = forms.DocumentCreatorForm(request.POST or None)
    output_settings_form = forms.OutputSettingsForm(request.POST or None)

    forms_dict = {
                "invoice_form": invoice_form,
                "advance_payment_form": advance_payment_form,
                "documents_form": documents_form,
                "seller_form": seller_form,
                "buyer_form": buyer_form,
                "shipper_form": shipper_form,
                "consignee_form": consignee_form,
                "additional_info_form": additional_info_form,
                "section_form": section_form,
                "product_form": product_form,
                "info_block_form": info_block_form,
                "transfer_details_form": transfer_details_form,
                "document_creator_form": document_creator_form,
                "output_settings_form": output_settings_form,
            }

    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'save':
            all_valid = True
            errors = []
            for form_name, form in forms_dict.items():
                if not form.is_valid():
                    all_valid = False
                    errors.append(f"Ошибка в форме {form_name}: {form.errors}")
            
            if all_valid:
                seller_instance = seller_form.save()
                shipper_instance = shipper_form.save(commit=False)
                shipper_instance.sellerbuyer_id = seller_instance
                shipper_instance.save()

                buyer_instance = buyer_form.save()
                consignee_instance = consignee_form.save(commit=False)
                consignee_instance.sellerbuyer_id = buyer_instance
                consignee_instance.save()
                
                section_instance = section_form.save()
                product_instance = product_form.save(commit=False)
                product_instance.section_id = section_instance
                product_instance.save()
                
                for form in forms_dict.values():
                    if form not in [shipper_form, consignee_form, product_form, seller_form, section_form]:
                        form.save()
                messages.success(request, "Данные успешно сохранены!")
                #return redirect('index')

                cleaned_data_dict = {form_name: form.cleaned_data for form_name, form in forms_dict.items()}
                def date_encoder(obj):
                    if isinstance(obj, date):
                        return obj.isoformat()
                    return obj
                return HttpResponse(json.dumps(cleaned_data_dict, default=date_encoder), content_type='application/json')
                
            else:
                messages.error(request, "Ошибки валидации:\n" + "\n".join(errors))
                # return render(request, "index.html", forms_dict)

    return render(request, "index.html", forms_dict)


def create_shipper(request):
    if request.method == 'POST':
        seller_form = SellerForm(request.POST)
        if seller_form.is_valid():
            seller = seller_form.save()
            shipper_form = ShipperForm(request.POST)
            if shipper_form.is_valid():
                shipper = shipper_form.save(sellerbuyer_id=seller.id)
                return redirect('success_page')
    else:
        seller_form = SellerForm()
        shipper_form = ShipperForm()
    return render(request, 'create_shipper.html', {'seller_form': seller_form, 'shipper_form': shipper_form})


def create_consignee(request):
    if request.method == 'POST':
        buyer_form = BuyerForm(request.POST)
        if buyer_form.is_valid():
            buyer = buyer_form.save()
            consignee_form = ConsigneeForm(request.POST)
            if consignee_form.is_valid():
                consignee = consignee_form.save(sellerbuyer_id=buyer.id)
                return redirect('success_page')
    else:
        buyer_form = BuyerForm()
        consignee_form = BuyerForm()
    return render(request, 'create_consignee.html', {'buyer_form': buyer_form, 'consignee_form': consignee_form})