from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import logout as django_logout


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Username atau password salah'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):

    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            bidang = form.cleaned_data.get("bidang")
            username = form.cleaned_data.get("username")
            name = form.cleaned_data.get("name")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(
                bidang=bidang, name=name, username=username, password=raw_password)

            msg = 'User created - please <a href="/login">Sign In</a>.'
            success = True
            form.save()

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def logout(request):
    django_logout(request)
    return redirect("/login/")
