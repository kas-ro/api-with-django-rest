import requests

endpoint = "http://127.0.0.1:8000/product/create/"
data = {
    "name": "Pomme", 
    "description": "Trop bon ce fruit", 
    "price": 200,
}
response = requests.post(endpoint, json=data)
print(response.json())
print(response.status_code)