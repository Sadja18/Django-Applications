from django.urls import path
from app_extended import views

#Template Tagging
app_name = 'app_extended'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
