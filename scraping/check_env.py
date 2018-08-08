import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/umemiya/Desktop/env/service_account_key.json"

print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])