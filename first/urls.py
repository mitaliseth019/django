"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from hello import views

from valentine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index ,name="index" ),   #means when we put "/hello" in our django page (url given when we run manage.py runserver) 
    #go to the hello app and look at the urls file in hello app and take us to the url where urls in hello points 

    #path('about', views.about ,name="about" ),
    #path('<str:name>', views.guest ,name="greet" ),
    path('', views.index ,name="valentine")
]
