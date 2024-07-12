from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request: HttpRequest):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if not user:
            return render(
                request,
                "auth/login.html",
                context={"error": "Email ou Mot de passe incorrect"},
            )
        login(request, user)
        next_url = request.GET.get("next", "/")
        return HttpResponseRedirect(next_url)

    return render(request, "auth/login.html")


def logout_view(request: HttpRequest):
    logout(request)
    return redirect("login")
