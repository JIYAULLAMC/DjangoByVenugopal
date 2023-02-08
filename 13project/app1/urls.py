from django.urls import path
from app1 import views
urlpatterns = [
    path('create_product/',views.create_product, name='create_product'),
    path('update_product/<int:pk>/',views.update_product, name='update_product'),
]