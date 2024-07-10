from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class WorkitUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_image = models.ImageField()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
