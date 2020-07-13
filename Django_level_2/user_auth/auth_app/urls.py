from django.urls import path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
                path('register/', views.register, name='register'),
                path('login/', views.login, name = 'login'),
]
