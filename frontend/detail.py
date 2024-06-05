import requests

endpoint = "http://127.0.0.1:8000/product/1"
data = {
    "name": "Pastesque", "description": "Bon fruit", "price": 2.5
}
response = requests.get(endpoint)
print(response.json())
print(response.status_code)