from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = form.cleaned_data["username"]
            user = authenticate(
                request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                # messages.success(
                # request, f"Welcome {name}, happy to have you here")
                return HttpResponse("User Is logged in finel")
            else:
                return HttpResponse("User invalid")

    else:
        form = LoginForm()
    return render(request, "Users/login.html", {"form": form})


@login_required
def index(request):
    return render(request, "Users/index.html")
