from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q


import account

from .models import Patient


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    else:
        if request.method == "POST":
            username =request.POST["username"]
            password =request.POST["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "account/login.html",
                {"error": "username or password is wrong!" })
        return render(request, "account/login.html")

def logout_request(request):
    logout(request)
    return(redirect("login"))


class PatientList(LoginRequiredMixin,ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = "account/patients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patients'] = context['patients'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['patients'] = context['patients'].filter(
                Q(name__startswith=search_input) | Q(tckn__startswith=search_input) | Q(surname__startswith=search_input))

            context['search_input'] = search_input
    
        
        
        return context

class PatientDetail(LoginRequiredMixin,DetailView):
    model = Patient
    context_object_name = 'patient'

class AddPatient(LoginRequiredMixin,CreateView):
    model = Patient
    template_name = "account/add_patient.html"
    fields = '__all__'
    success_url = reverse_lazy('hastalar')

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super(AddPatient,self).form_valid(form)

class UpdatePatient(LoginRequiredMixin,UpdateView):
    model = Patient
    template_name = "account/update_patient.html"
    fields = '__all__'
    success_url = reverse_lazy('hastalar')

class DeletePatient(LoginRequiredMixin,DeleteView):
    model = Patient
    context_object_name = 'patient'
    success_url = reverse_lazy('hastalar')
    template_name = "account/delete_patient_confirm.html"

