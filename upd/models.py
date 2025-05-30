from email.policy import default
from django.db import models
from django.forms import CharField
from django.utils.timezone import now


class Invoice(models.Model):
    invoice_number = models.CharField(blank=True)
    date = models.DateField(default=now, blank=True, null=True)
    is_adjusted = models.BooleanField(default=False, blank=True)
    adjusted_number = models.CharField(blank=True)
    adjusted_date = models.DateField(default=now, blank=True, null=True)

    def __str__(self):
        return self.name


class AdvancePayment(models.Model):
    is_advance = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class PaymentDocument(models.Model):
    number = models.CharField(blank=True)
    date = models.DateField(default=now, blank=True, null=True)

    def __str__(self):
        return self.name


class ShippingDocument(models.Model):
    name = models.CharField(blank=True)
    number = models.CharField(blank=True)
    date = models.DateField(default=now, blank=True, null=True)

    def __str__(self):
        return self.name


# class SellerBuyer(models.Model):
#     type = models.CharField(blank=True)
#     status = models.CharField(blank=True)
#     name = models.CharField(blank=True)
#     full_name = models.CharField(blank=True)
#     inn = models.CharField(blank=True)
#     kpp = models.CharField(blank=True)
#     reg_address = models.CharField(blank=True)
#     address = models.CharField(blank=True)
#     requisite = models.CharField(blank=True)
#     manager = models.CharField(blank=True)
#     manager_fio = models.CharField(blank=True)
#     accountant_fio = models.CharField(blank=True)

#     def __str__(self):
#         return self.name


class Seller(models.Model):
    status = models.CharField(blank=True)
    name = models.CharField(blank=True)
    full_name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)
    reg_address = models.CharField(blank=True)
    address = models.CharField(blank=True)
    requisite = models.CharField(blank=True)
    manager = models.CharField(blank=True)
    manager_fio = models.CharField(blank=True)
    accountant_fio = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)
    address = models.CharField(blank=True)
    manager = models.CharField(blank=True)
    manager_fio = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Shipper(models.Model):
    relation_type = models.CharField(blank=True)
    name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)
    address = models.CharField(blank=True)
    manager_fio = models.CharField(blank=True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Consignee(models.Model):
    relation_type = models.CharField(blank=True)
    name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)
    address = models.CharField(blank=True)
    manager_fio = models.CharField(blank=True)
    buyer_id = models.ForeignKey(Buyer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AdditionalInfo(models.Model):
    contact_identifier = models.CharField(blank=True)
    document_type = models.CharField(blank=True)
    vat_rate = models.CharField(blank=True)
    nds_activ = models.CharField(blank=True)
    currency = models.CharField(blank=True)
    form_format = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    article = models.CharField(blank=True)
    unit = models.CharField(blank=True)
    quantity = models.CharField(blank=True)
    customs_code = models.CharField(blank=True)
    customs_type_code = models.CharField(blank=True)
    excise_duty = models.CharField(blank=True)
    number = models.CharField(default=1, blank=True)
    country_code = models.CharField(blank=True)
    country_name = models.CharField(blank=True)
    full_sum = models.FloatField(default=0.0, blank=True)
    customs_declaration_num = models.TextField(blank=True)
    price = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return self.name


class InfoBlock(models.Model):
    basis = models.CharField(blank=True)
    transportation_data = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Transfered(models.Model):
    position = models.CharField(blank=True)
    name = models.CharField(blank=True)
    date = models.DateField(default=now, blank=True, null=True)
    is_signed = models.BooleanField(blank=True)
    other = models.CharField(blank=True)
    resp_position = models.CharField(blank=True)
    resp_name = models.CharField(blank=True)

    def __str__(self):
        return self.name


class Received(models.Model):
    position = models.CharField(blank=True)
    name = models.CharField(blank=True)
    date = models.DateField(default=now, blank=True, null=True)
    other = models.CharField(blank=True)
    resp_position = models.CharField(blank=True)
    resp_name = models.CharField(blank=True)

    def __str__(self):
        return self.name


class DocumentSeller(models.Model):
    role = models.CharField(blank=True)
    name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)

    def __str__(self):
        return self.name


class DocumentBuyer(models.Model):
    role = models.CharField(blank=True)
    name = models.CharField(blank=True)
    inn = models.CharField(blank=True)
    kpp = models.CharField(blank=True)

    def __str__(self):
        return self.name


class OutputSettings(models.Model):
    show_stamp = models.BooleanField(blank=True)
    show_signature = models.BooleanField(blank=True)
    file_format = models.CharField(blank=True)

    def __str__(self):
        return self.name
