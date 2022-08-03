from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return render(
                request, "registration/register_done.html", {"new_user": user}
            )
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})
