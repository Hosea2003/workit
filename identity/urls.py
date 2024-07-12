from django.urls import path

from identity.views import change_password, login_view, logout_view, profile_user

urlpatterns = [
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("my-profile", profile_user, name="my-profile"),
    path("change-password", change_password, name="change-password"),
]
