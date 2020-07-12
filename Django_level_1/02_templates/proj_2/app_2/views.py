from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "app_2/index.html")

def help(request):
    help_dict = {"help_insert": "Help Page"}
    return render(request, "app_2/help.html", context = help_dict)
