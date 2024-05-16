from django.urls import path
from . import views

app_name = "recommand"

urlpatterns = [
    path("", views.main, name="main"),
    path("man/", views.man, name = "man"),  
    path("woman/", views.woman, name = "woman"),  
    path("upload/", views.upload, name = "upload"),
]