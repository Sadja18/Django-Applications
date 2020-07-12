from django.shortcuts import render
from form_app import forms
# Create your views here.
def home(request):
    return render(request,"form_app/home.html")

def form_page(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Working
            print("Validated successfully")
            print("Name: "+ str(form.cleaned_data["name"]))
            print("Email: "+ str(form.cleaned_data["email"]))
    return render(request, "form_app/form_page.html", {"form":form})
