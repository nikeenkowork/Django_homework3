from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            send_mail(
                subject="Добро пожаловать!",
                message=(
                    "Спасибо за регистрацию "
                    "на нашем сервисе!"
                ),
                from_email="admin@example.com",
                recipient_list=[
                    user.email
                ],
            )

            login(request, user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {"form": form}
    )


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            user = form.cleaned_data["user"]

            login(request, user)

            return redirect("home")

    else:
        form = LoginForm()

    return render(
        request,
        "users/login.html",
        {"form": form}
    )


def logout_view(request):
    logout(request)

    return redirect("login")
