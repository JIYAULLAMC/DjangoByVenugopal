from django.urls import path
from app1 import views
urlpatterns=[
    path('home/',views.homeview,name="home"),
    path('detail/',views.detailview,name="detail"),
    path('update/<pk>/',views.updateview,name="update"),
    path('delete/<pk>/',views.deleteview,name="delete"),
    ]