from django.urls import path
from myemp import views


urlpatterns = [
    path('funcview/', views.funcview, name="funcview"),
    path('empview/', views.EmpView.as_view(), name="funcview")
]