import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #"http://127.0.0.1:8000/"

# , json={"query" : "Hello world"}
get_response = requests.post(endpoint, params={"product_id" : 123}) # HTTP Request
# print(get_response.headers) # print raw test response
# print(get_response.text) # print raw test response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
print(get_response.json()) # print raw test response
# print(get_response.status_code) # print raw test response