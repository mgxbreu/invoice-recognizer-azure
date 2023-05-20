from utils.credentials import get_credentials
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient

class RecognizeInvoice(object):

    def __init__(self, path):
        self.path = path
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
        self.invoices = None
        KEY, ENDPOINT = get_credentials("formRecognizer")
        self.form_recognizer_client = FormRecognizerClient(
            endpoint=ENDPOINT, credential=AzureKeyCredential(KEY)
        )

    def recognize_invoice(self):
        with open(self.path, "rb") as invoice_file:
            poller = self.form_recognizer_client.begin_recognize_invoices(invoice=invoice_file, locale="en-US")
        self.invoices = poller.result()

    def extract_information(self):
        for invoice in self.invoices:
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
                    self.address = vendor_address_recipient.value
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
            try:
                self.product_quantity = len(invoice.fields.get("Items").value)
            except:
                pass

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
            try:
                payment_details = invoice.fields.get("PaymentDetails")
                if payment_details:
                    self.payment_method = payment_details
                    print("❤️‍🔥 PaymentDetails: {} has confidence: {}".format(payment_details.value, payment_details.confidence))
            except:
                pass
           
    def start_process(self):
        self.recognize_invoice()
        self.extract_information()

    def serialize_information(self):
        return {
            "file_name": self.path,
            "business_name" : self.business_name,
            "business_address": self.business_address,
            "country": self.country,
            "address": self.address,
            "date": self.date,
            "payment_method": self.payment_method,
            "total": self.total,
            "product_quantity": self.product_quantity,
            "subtotal": self.subtotal,
            "tax": self.tax,
            "product_type": self.product_type,
        }