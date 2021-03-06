from .forms import LoginForm, UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["email"], password=cd["password"])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated Successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid Login")
    else:
        form = UserCreationForm()
    return render(request, "account/login.html", {"form": form})


@login_required
def dashboard(request):

    context = {"section": "dashboard"}
    return render(request, "dashboard.html", context)
