from  django.urls import path
from product import views
urlpatterns=[
    path('createp/',views.productview,name="createp"),
    path('updatep/<int:pk>/',views.productupdate,name="updatep"),
    ]