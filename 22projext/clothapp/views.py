from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from clothapp.models import Cloth


# ------------------api---------------
from clothapp.serializers import ClothSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView, UpdateAPIView


def chome(request):
    return render(request, 'boot.html')


class ClothList(ListAPIView):
    template_name = "chome.html"
    model = Cloth
    queryset = Cloth.objects.all()
    fields= "__all__"
    context_object_name = "allcloths"
    serializer_class = ClothSerializer

class ClothDetail(RetrieveAPIView):
    template_name = "clothdetail.html"
    queryset = Cloth.objects.all()
    model = Cloth
    fields= "__all__"
    context_object_name = "cloth"
    serializer_class = ClothSerializer


class ClothCreate(CreateAPIView):
    template_name = "clothcreate.html"
    model = Cloth
    fields = "__all__"
    queryset = Cloth.objects.all()
    context_object_name = "form"
    success_url = './chome/'
    serializer_class = ClothSerializer

class ClothUpdate(UpdateAPIView):
    template_name = "clothcreate.html"
    model = Cloth
    fields = "__all__"
    queryset = Cloth.objects.all()
    context_object_name = "form"
    success_url = './chome/'
    serializer_class = ClothSerializer




    



