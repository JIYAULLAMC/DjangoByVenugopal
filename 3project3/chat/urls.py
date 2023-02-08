from django.urls import path
from chat import views

app_name = "chat"
# handler404 = 'chat.views.not_found_view'

urlpatterns = [
    path("ccontact/", views.ccontact, name="ccontact"),
    path("chome/", views.chome, name="chome"),
]
