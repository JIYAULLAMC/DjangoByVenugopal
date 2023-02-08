from django.urls import path
from bank import views

urlpatterns = [
    path('create/<bid>/<bname>/<ifsc>/',views.createview,name='create'),
    path('update/<bid>/<bname>/',views.updateview,name='update'),
    path('delete/<bid>',views.deleteview,name='delete'),
    path('list/',views.listview,name='list'),
]