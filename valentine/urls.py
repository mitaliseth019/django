from django.urls import path

from . import views   #i.e from current dir. (for that we use .) import views file

urlpatterns=[ #this is a list if user enter these urls than our index function in views will be called
    path('', views.index , name='index')
]