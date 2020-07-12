from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app_extended/index.html")

def other(request):
    return render(request, 'app_extended/other.html')

def relative(request):
    return render(request, 'app_extended/relative_url_template.html')
