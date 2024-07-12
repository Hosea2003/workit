from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from api.decorators import workit_staff
from identity.forms import ProfileForm
from django.utils.translation import gettext_lazy as _

from identity.models import WorkitUser


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


@workit_staff
def profile_user(request: HttpRequest):
    update_profile_form = ProfileForm(instance=request.user)
    message = None

    if request.method == "POST":
        update_profile_form = ProfileForm(request.POST, instance=request.user)
        if update_profile_form.is_valid():
            user = update_profile_form.save(commit=False)
            if request.FILES:
                user.profile_image = request.FILES.get("profile_image")
            user.save()
            message = _("Enregistrer avec succès")

    return render(
        request,
        "auth/profile.html",
        context={"form": update_profile_form, "message": message},
    )
