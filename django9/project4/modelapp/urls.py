from django.urls import path
from modelapp import views
urlpatterns=[
    path('register/',views.registerview,name="register"),
    path('update/<int:pk>/',views.updateview,name="update"),
    path('index/',views.index,name="index"),
    ]