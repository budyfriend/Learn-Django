import requests

endpoint = "http://localhost:8002/api/products/1/update/" 

data = {
    "title":"Hello world",
    "price": 00.0
}
get_response = requests.put(endpoint, json=data) 
print(get_response.json()) 