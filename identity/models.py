from django.db import models
from django.contrib.auth.models import AbstractUser

from identity.managers import WorkitUserManager


# Create your models here.
class WorkitUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_image = models.ImageField(null=True, blank=True)

    objects = WorkitUserManager()

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
