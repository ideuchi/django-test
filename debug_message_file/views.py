from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    debug_message = 'default'
    with open('debug.txt') as f1:
       debug_message = f1.read()
    return HttpResponse('<pre>' + debug_message + '</pre>')
