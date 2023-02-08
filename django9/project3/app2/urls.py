from django.urls import  path
from app2 import views

urlpatterns=[
    path('register/',views.productview,name="register"),
    path('update/<pk>/',views.productupdate,name="update"),
    path('read/',views.productread,name="read"),
    path('delete/<pk>/',views.productdelete,name="delete"),

    ]