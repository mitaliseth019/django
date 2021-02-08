from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):  #request argument is going to represent http request that user want to access in web server
    return render(request,"hello/index.html")

# now we have to do tell this app that when u have to return this "Hello world" i.e at what url of user this response will be returned  

def about(request):  #request argument is going to represent http request that user want to access in web server
    return HttpResponse("About Hello world")

def guest(request,name):
    return render(request, "hello/greet.html", {
         "name":name.capitalize()
    }) 