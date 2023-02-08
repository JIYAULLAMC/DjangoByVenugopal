from django.urls import path
from myapp import views
urlpatterns=[
    path('register/',views.registerview,name="register"),
    path('list/',views.listview,name="list"),
    path('detail/<int:pk>/',views.detailview,name="detail"),
    path('update/<int:pk>/',views.updateview,name="update"),
    path('delete/<int:pk>/',views.deleteview,name="delete"),
    ]