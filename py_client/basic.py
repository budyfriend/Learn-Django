import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8002/api/" #"http://127.0.0.1:8000/"

# , json={"query" : "Hello world"}
get_response = requests.post(endpoint, json={"title": "Abc123","content": "Hello world"}) # HTTP Request
# print(get_response.headers) # print raw test response
# print(get_response.text) # print raw test response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
print(get_response.json()) # print raw test response
# print(get_response.status_code) # print raw test response