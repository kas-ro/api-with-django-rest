import requests

endpoint = "http://127.0.0.1:8000/product/1/update/"
data = {
    "name": "Kiwi", "description": "Bon et trop juteux fruit", "price": 455
}
response = requests.put(endpoint, json=data)
print(response.json())
print(response.status_code)