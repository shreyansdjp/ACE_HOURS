from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    # GET, POST, PUT, PATCH, HEAD, DELETE request methods
    if request.method == 'GET':
        data = request.GET
        name = data['name']
        return HttpResponse(f"<title>Hello, World!</title> <h2>Hello, {name}</h2>")
    else:
        return HttpResponse('You can not access this')
