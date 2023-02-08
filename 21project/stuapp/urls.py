from django.urls import path
from stuapp import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('screate/', views.screate, name='screate'),
    path('slogin/', views.slogin, name='slogin'),
    path('slogout/', views.slogout, name='slogin'),
]