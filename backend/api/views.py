import json
from wsgiref import headers
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# Django Models

# ["GET", "POST"]
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    BudyfriendCode API View
    """
    # if request.method != "POST":
    #     return Response({"detail":"GET not allowed"}, status=405)

    # # requests -> HttpRequest -> Django
    # # print(dir(request))
    # # request.body
    # print(request.GET) # url query params
    # print(request.POST)
    # body = request.body # byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) # string of Json data -> Python Dict
    # except:
    #     pass
    # print(data)
    # # data['headers'] = request.headers # request.META -> 
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return JsonResponse({"message" : "Hi there, this is your Django API respone!!"})


    instance = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
        # model instance (model_data)
        # turn a Python dict
        # return JSON to my client

    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type" : "application/json"})