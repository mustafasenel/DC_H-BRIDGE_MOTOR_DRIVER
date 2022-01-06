from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    
    if request.user.is_authenticated:
        return render(request, "base.html")
    else:
        return render(request, "account/login.html")


def auto(request):
    return render(request, "autoAngle/auto.html")