from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm  # Authentication form
from django.shortcuts import redirect, render

from .forms import NewUserForm

# Create your views here.


def register_request(request):
    if request.method == "POST":
        print(request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("in if condition")
            user = form.save()
            # login(request, user)
            return redirect("register")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user,user.__dict__)
            if user:
                login(request, user) #entry save in database----it saves a session in database to for all page
                return redirect("home_page")
            else:
                return redirect("login_user")
        else:
            return redirect("login_user")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    return redirect("login_user")
    