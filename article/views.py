from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #返回HttpResponse对象
    return HttpResponse("<html><body><h1>Hello world</h1></body></html>")
 
