"""pro3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pro3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/",views.base,name="base"),
    path("home/",views.home,name="home"),
    path("chat/",include("chat.urls")),
    path("payment/",include("payment.urls")),
    path("account/",include("account.urls")),
    # this used to send or request the data from one file to another file 
    path("database/",views.database,name="database"),
    path("datahome/<ind>/<data>/",views.datahome,name="datahome"),
    path("sbase/",views.sbase, name="sbase"),
    path("shome/<data>/",views.shome, name="shome"),
]
