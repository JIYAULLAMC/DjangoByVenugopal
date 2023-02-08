from django import views
from django.urls import path
from app3 import views

urlpatterns =[
    path("home3/<status>/",views.home3, name="home3"),
    path("filters/",views.filters, name="filters"),
]