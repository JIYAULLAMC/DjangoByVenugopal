from django.urls import path
from app2 import views
urlpatterns = [
    path("ap2home/",views.home, name="ap2home"),
    path("register/",views.register, name="register"),


]