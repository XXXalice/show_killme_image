import requests

url = "https://xxxalice.github.io/"

payload = {
    'key1' : "value1",
    "key2" : "value2"
}

uri_add_query = requests.get(url=url, params=payload)

print(uri_add_query.text)