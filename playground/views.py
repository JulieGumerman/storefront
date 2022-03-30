from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes a request and returns a response
# request handler
# in django, this is a view

def say_hello(request):
    return HttpResponse('Hello World')
