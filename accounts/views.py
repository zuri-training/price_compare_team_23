from django.shortcuts import redirect, render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.views.generic import ListView
import django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "category/index.html", {"user": user})
        else:
            # Return an 'invalid login' error message.
            return redirect("accounts:signin")

    return render(request, "registration/login.html")


def user_profile(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["old_password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            new_password = request.POST["change-password"]
            login(request, user)
            user.set_password(new_password)
            return render(request, "category/index.html", {"user": user})
        else:
            # Return an 'invalid login' error message.
            return redirect("accounts:user_profile")

    return render(request, "user_profile.html")


def register(request):
    if request.method == "POST":
        input = request.POST
        try:
            user = User.objects.create_user(
                input["username"],
                email=input["email"],
                password=input["password"],
                first_name=input["first_name"],
                last_name=input["last_name"],
            )
            user.save()
            login(request, user)
        except django.db.utils.IntegrityError:
            return render(
                request, "registration/signUp.html", {"msg": "user already exists"}
            )

        return redirect("category:home")

    return render(request, "registration/signUp.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
