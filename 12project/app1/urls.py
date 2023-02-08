from django.urls import path
from app1 import views
urlpatterns = [
    path('create_student/',views.create_student,name='create_student'),
    path('update_student/<int:pk>/',views.update_student,name='update_student'),
    path('read_student/',views.read_student,name='read_student'),
]