from django.urls import path
from clothapp import views


urlpatterns = [
    path("chome/",views.chome,name="chome"),
    path("clothlist/",views.ClothList.as_view(),name="clothlist"),
    path("clothcreate/",views.ClothCreate.as_view(),name="clothcreate"),
    path("clothupdate/<int:pk>/",views.ClothUpdate.as_view(),name="clothupdate"),
    path("clothdetail/<int:pk>/",views.ClothDetail.as_view(),name="clothdetail"),
]