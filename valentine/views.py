import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request, "valentine/index.html", {
        "valentine":now.day==14 and now.month==2
    })