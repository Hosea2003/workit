from django.urls import path

from identity.views import login_view, logout_view, profile_user

urlpatterns = [
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("my-profile", profile_user, name="my-profile"),
]
