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
            except:
                pass
            try:
                invoice_date = invoice.fields.get("InvoiceDate")
                if invoice_date:
                    self.date = invoice_date.value
            except:
                pass
            try:
                invoice_total = invoice.fields.get("InvoiceTotal")
                if invoice_total:
                    self.total = invoice_total.value
            except:
                pass
            try:
                billing_address = invoice.fields.get("BillingAddress")
                if billing_address:
                    print("Billing Address: {} has confidence: {}".format(billing_address.value, billing_address.confidence))
            except:
                pass
            try:
                billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
                if billing_address_recipient:
                    print("Billing Address Recipient: {} has confidence: {}".format(billing_address_recipient.value, billing_address_recipient.confidence))
            except:
                pass
            print("Invoice items:")
            # print(invoice.fields.values()) 
            # for idx, item in enumerate(invoice.fields.get("Items").value):
            #     print("...Item #{}".format(idx+1))
            #     item_description = item.value.get("Description")
            try:
                subtotal = invoice.fields.get("SubTotal")
                if subtotal:
                    self.subtotal = subtotal.value
            except:
                pass
            try:
                total_tax = invoice.fields.get("TotalTax")
                if total_tax:
                    self.tax = total_tax.value
            except:
                pass
            try:    
                service_address = invoice.fields.get("ServiceAddress")
                if service_address:
                    print("Service Address: {} has confidence: {}".format(service_address.value, service_address.confidence))
            except:
                pass
            
            try:
                remittance_address = invoice.fields.get("RemittanceAddress")
                if remittance_address:
                    print("Remittance Address: {} has confidence: {}".format(remittance_address.value, remittance_address.confidence))
            except:
                pass

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