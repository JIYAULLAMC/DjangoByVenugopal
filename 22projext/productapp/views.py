from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from productapp.models import Product
# Create your views here.


#-------------api----------------
from productapp.serializers import ProductSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView,RetrieveAPIView



def phome(request):
    return render(request, 'phome.html')


class ProductList(ListAPIView):
    template_name = "phome.html"
    model =Product
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    fields= "__all__"
    context_object_name = "products"

class ProductDetail(RetrieveAPIView):
    template_name = "productdetail.html"
    model =Product
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    fields= "__all__"
    context_object_name = "product"


class ProductCreate(CreateAPIView):
    template_name = "productcreate.html"
    model =Product
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    fields = "__all__"
    context_object_name = "form"
    success_url = './chome/'
    

class ProductUpdate(UpdateAPIView):
    template_name = "productcreate.html"
    model = Product
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    fields = "__all__"
    context_object_name = "form"
    success_url = './chome/'




    



