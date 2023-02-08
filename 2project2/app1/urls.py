from django import views
from  django.urls import path
from app1 import views
urlpatterns = [
    path("app_view/",views.app_view, name="app_view"),
    path("home/",views.home, name="home"),
]