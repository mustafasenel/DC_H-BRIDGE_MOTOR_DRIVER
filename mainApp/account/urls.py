#http://127.0.0.1:8000/              == index
#http://127.0.0.1:8000/index         == index

from django.urls import path
from. import views

urlpatterns = [
    path("",views.login_request, name="login"),
    path("",views.logout_request, name="logout")
    

]