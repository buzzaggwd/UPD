from django.contrib import messages
from django.shortcuts import render, redirect
from . import forms


def index(request):
    json_data = None

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
                # # Сохраняем формы без внешних ключей (commit=False)
                # shipper_instance = shipper_form.save(commit=False)
                # consignee_instance = consignee_form.save(commit=False)
                # product_instance = product_form.save(commit=False)
                
                # # Устанавливаем внешние ключи (пример: sellerbuyer берется из seller_form)
                # seller_instance = seller_form.save()  # Предполагается, что seller_form валиден
                # shipper_instance.sellerbuyer_id = seller_instance
                # consignee_instance.sellerbuyer_id = seller_instance
                
                # # Устанавливаем section_id (пример: section берется из section_form)
                # # В блоке if action == 'save':
                # section_instance = section_form.save()  # Сохраняем раздел
                # product_instance = product_form.save(commit=False)
                # product_instance.section_id = section_instance  # Устанавливаем внешний ключ
                # product_instance.save()  # Теперь сохраняем продукт
                
                # # Теперь сохраняем полные экземпляры
                # shipper_instance.save()
                # consignee_instance.save()
                # product_instance.save()
                
                # Сохраняем остальные формы
                for form in forms_dict.values():
                    if form not in [shipper_form, consignee_form, product_form]:
                        form.save()
                messages.success(request, "Данные успешно сохранены!")
                return redirect('index')
            else:
                messages.error(request, "Ошибки валидации:\n" + "\n".join(errors))
                return render(request, "index.html", forms_dict)

    return render(request, "index.html", forms_dict)

