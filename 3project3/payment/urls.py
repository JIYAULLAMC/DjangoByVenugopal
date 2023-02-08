from django.urls import path
from payment import views

app_name = "payment"
# handler404 = 'chat.views.not_found_view'

urlpatterns = [
    path("pcontact/", views.pcontact, name="pcontact"),
    path("phome/", views.phome, name="phome"),
]
