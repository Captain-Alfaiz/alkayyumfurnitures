from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sendemail', views.sendemail, name="sendemail"),
]
