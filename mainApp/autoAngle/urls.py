#http://127.0.0.1:8000/              == index
#http://127.0.0.1:8000/index         == index

from django.urls import path
from. import views

urlpatterns = [
    path("index",views.index, name="home"),
    path("auto",views.auto, name="autoMode")

]