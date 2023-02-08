from django.urls import path
from productapp import views
urlpatterns = [
    path("phome/",views.phome, name="phome"),
    path("productlist/",views.ProductList.as_view(),name="productlist"),
    path("productcreate/",views.ProductCreate.as_view(),name="productcreate"),
    path("productupdate/<int:pk>/",views.ProductUpdate.as_view(),name="productupdate"),
    path("productdetail/<int:pk>/",views.ProductDetail.as_view(),name="productdetail"),


]