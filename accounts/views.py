from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.contrib import messages

from .models import Profile
from .forms import LoginForm, SignUpForm


def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username atau password salah')
        else:
            messages.info(request, 'Error validasi form')

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def user_register(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            bidang = form.cleaned_data.get('bidang')
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            Profile.objects.create(
                user=user,
                nama=user.username,
                bidang=bidang
            )

            messages.success(request, 'Akun telah di buat ' + username)
            return redirect("login")

    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context)


def user_logout(request):
    logout(request)
    return redirect("/login/")
