from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Yestech Developers')

def about(request):
    return HttpResponse('Yestech Developers is integrating small tech business')

