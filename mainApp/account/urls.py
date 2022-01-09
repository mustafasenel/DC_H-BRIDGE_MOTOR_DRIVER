#http://127.0.0.1:8000/              == index
#http://127.0.0.1:8000/index         == index

from django.urls import path
from. import views
from .views import PatientDetail, PatientList,AddPatient,UpdatePatient,DeletePatient

urlpatterns = [
    path("",views.login_request, name="login"),
    path("logout",views.logout_request, name="logout"),


    path("hastalar", PatientList.as_view(),name="hastalar"),
    path("hastalar/<int:pk>/", PatientDetail.as_view(),name="hastalar"),
    path("hastalar/hasta-ekle/", AddPatient.as_view(),name="hasta-ekle"),
    path("hastalar/hasta-edit/<int:pk>/", UpdatePatient.as_view(),name="hasta-edit"),
    path("hastalar/hasta-sil/<int:pk>/", DeletePatient.as_view(),name="hasta-sil"),

]