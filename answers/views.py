from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, name="жопулечка"):
    output = "<h2>User</h2><h3>name: {0}</h3>".format(name)
    return HttpResponse(output)


