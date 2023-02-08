from django import views
from django.urls import path
from myprofile import views

app_name = "myprofile"

urlpatterns = [
    # path("myprofile/",views.myprofile,name="myprofile"),
    # path("about/",views.about,name="about"),
    path("base/",views.base,name="base"),
]