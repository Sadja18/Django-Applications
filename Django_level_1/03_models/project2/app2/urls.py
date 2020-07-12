from django.urls import path
from app2 import views

urlpatterns =[
    path("users/",views.users, name="users"), 
]
