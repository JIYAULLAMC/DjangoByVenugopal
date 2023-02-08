import imp
from django.urls import path
from stuapp import views
urlpatterns = [
    path('home/',views.home, name='home'),
    path('slist/',views.slist, name='slist'),
    path('screate/',views.screate, name='screate'),
    path('supdate/<int:pk>/',views.supdate,name='supdate'),
    path('sdelete/<int:pk>/',views.sdelete,name='sdelete'),
    path('slogin/',views.slogin, name='slogin'),
    path('slogout/',views.slogout, name='slogout'),
]