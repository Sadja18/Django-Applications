from django.conf.urls import url
from proj_app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
