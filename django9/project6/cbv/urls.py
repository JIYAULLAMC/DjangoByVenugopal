from django.urls import path
from cbv import views
urlpatterns=[
    path("func/",views.func,name="func"),
    path('ucbv/',views.ucbv.as_view(),name="ucbv"),
    path('pcbv/',views.pcbv.as_view(),name="pcbv"),
    path('ccbv/',views.ccbv.as_view(),name="ccbv"),
]