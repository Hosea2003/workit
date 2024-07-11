from django.contrib.auth.models import BaseUserManager


class WorkitUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email missing")

        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        return self.create_user(email, password=password, **kwargs)
