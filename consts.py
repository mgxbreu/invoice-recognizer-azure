from utils.credentials import get_credentials
import uuid

KEY, ENDPOINT = get_credentials("translator")
region = 'eastus'

headers = [
    "file_name",
    "business_name",
    "business_address",
    "country",
    "address",
    "date",
    "time",
    "payment_method",
    "total",
    "product_quantity",
    "subtotal",
    "tax",
    "product_type",
]

service_headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }