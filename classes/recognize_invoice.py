import json
import os
from utils import get_credentials
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

class RecognizeInvoice(object):

    def __init__(self, path):
        self.file_name = ""
        self.business_name = ""
        self.business_address = ""
        self.country = ""
        self.address = ""
        self.date = ""
        self.time = ""
        self.payment_method = ""
        self.total = None
        self.product_quantity = None
        self.subtotal = None
        self.tax = None
        self.product_type = ""
        self.path = path


    def recognize_invoice(self):
        KEY, ENDPOINT = get_credentials("formRecognizer")

        form_recognizer_client = FormRecognizerClient(
            endpoint=ENDPOINT, credential=AzureKeyCredential(KEY)
        )
        with open(self.path, "rb") as f:
            poller = form_recognizer_client.begin_recognize_invoices(invoice=f, locale="en-US")
        invoices = poller.result()

        for idx, invoice in enumerate(invoices):
            try:
                vendor_name = invoice.fields.get("VendorName")
                if vendor_name:
                    self.business_name = vendor_name.value
            except:
                pass
            try:
                vendor_address = invoice.fields.get("VendorAddress")
                if vendor_address:
                    self.business_address = vendor_address.value
            except:
                pass
            try:
                vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
                if vendor_address_recipient:
                    print("Vendor Address Recipient: {} has confidence: {}".format(vendor_address_recipient.value, vendor_address_recipient.confidence))
            customer_address = invoice.fields.get("CustomerAddress")
            if customer_address:
                print("Customer Address: {} has confidence: {}".format(customer_address.value, customer_address.confidence))
            customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
            if customer_address_recipient:
                print("Customer Address Recipient: {} has confidence: {}".format(customer_address_recipient.value, customer_address_recipient.confidence))
                invoice_date = invoice.fields.get("InvoiceDate")
                if invoice_date:
                    self.date = invoice_date.value
            except:
                pass
            try:
                invoice_total = invoice.fields.get("InvoiceTotal")
                if invoice_total:
                    self.total = invoice_total.value
            purchase_order = invoice.fields.get("PurchaseOrder")
            if purchase_order:
                print("Purchase Order: {} has confidence: {}".format(purchase_order.value, purchase_order.confidence))
                billing_address = invoice.fields.get("BillingAddress")
                if billing_address:
                    print("Billing Address: {} has confidence: {}".format(billing_address.value, billing_address.confidence))
            except:
                pass
            try:
                billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
                if billing_address_recipient:
                    print("Billing Address Recipient: {} has confidence: {}".format(billing_address_recipient.value, billing_address_recipient.confidence))
            shipping_address = invoice.fields.get("ShippingAddress")
            if shipping_address:
                print("Shipping Address: {} has confidence: {}".format(shipping_address.value, shipping_address.confidence))
            shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
            if shipping_address_recipient:
                print("Shipping Address Recipient: {} has confidence: {}".format(shipping_address_recipient.value, shipping_address_recipient.confidence))
            print("Invoice items:")
            # print(invoice.fields.values()) 
            # for idx, item in enumerate(invoice.fields.get("Items").value):
            #     print("...Item #{}".format(idx+1))
            #     item_description = item.value.get("Description")
            #     if item_description:
            #         print("......Description: {} has confidence: {}".format(item_description.value, item_description.confidence))
            #     item_quantity = item.value.get("Quantity")
            #     if item_quantity:
            #         print("......Quantity: {} has confidence: {}".format(item_quantity.value, item_quantity.confidence))
            #     unit = item.value.get("Unit")
            #     if unit:
            #         print("......Unit: {} has confidence: {}".format(unit.value, unit.confidence))
            #     unit_price = item.value.get("UnitPrice")
            #     if unit_price:
            #         print("......Unit Price: {} has confidence: {}".format(unit_price.value, unit_price.confidence))
            #     product_code = item.value.get("ProductCode")
            #     if product_code:
            #         print("......Product Code: {} has confidence: {}".format(product_code.value, product_code.confidence))
            #     item_date = item.value.get("Date")
            #     if item_date:
            #         print("......Date: {} has confidence: {}".format(item_date.value, item_date.confidence))
            #     tax = item.value.get("Tax")
            #     if tax:
            #         print("......Tax: {} has confidence: {}".format(tax.value, tax.confidence))
            #     amount = item.value.get("Amount")
            #     if amount:
            #         print("......Amount: {} has confidence: {}".format(amount.value, amount.confidence))
                subtotal = invoice.fields.get("SubTotal")
                if subtotal:
                print("Subtotal: {} has confidence: {}".format(subtotal.value, subtotal.confidence))
                total_tax = invoice.fields.get("TotalTax")
                if total_tax:
                print("Total Tax: {} has confidence: {}".format(total_tax.value, total_tax.confidence))
                service_address = invoice.fields.get("ServiceAddress")
                if service_address:
                    print("Service Address: {} has confidence: {}".format(service_address.value, service_address.confidence))
            service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
            if service_address_recipient:
                print("Service Address Recipient: {} has confidence: {}".format(service_address_recipient.value, service_address_recipient.confidence))
                remittance_address = invoice.fields.get("RemittanceAddress")
                if remittance_address:
                    print("Remittance Address: {} has confidence: {}".format(remittance_address.value, remittance_address.confidence))
            remittance_address_recipient = invoice.fields.get("RemittanceAddressRecipient")
            if remittance_address_recipient:
                print("Remittance Address Recipient: {} has confidence: {}".format(remittance_address_recipient.value, remittance_address_recipient.confidence))
        # [END recognize_invoices]

    def get_info(self):
        return {
            "file_name": self.file_name,
            "business_name" : self.business_name,
            "business_address": self.business_address,
            "country": self.country,
            "address": self.address,
            "date": self.date,
            "time": self.time,
            "payment_method": self.payment_method,
            "total": self.total,
            "product_quantity": self.product_quantity,
            "subtotal": self.subtotal,
            "tax": self.tax,
            "product_type": self.product_type,
        }