from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_contnt': " Hello I am from proj_app"}
    return render(request, 'proj_app/index.html', context=my_dict)
