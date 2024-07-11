from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login


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
        return redirect("dashboard")

    return render(request, "auth/login.html")
