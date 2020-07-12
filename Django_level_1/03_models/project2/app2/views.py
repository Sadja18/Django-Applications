from django.shortcuts import render
#from app2.models import User

from app2.forms import NewUserForm

# Create your views here.
def home(request):
    return render(request, "app2/home.html")

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("Invalid Form")

    return render(request, "app2/user.html", {'form':form})
