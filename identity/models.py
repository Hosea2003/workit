from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from identity.managers import WorkitUserManager
from django.templatetags.static import static


# Create your models here.
class WorkitUser(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    profile_image = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GenderChoices.choices, default=GenderChoices.MALE
    )

    objects = WorkitUserManager()

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def public_image(self):
        if not self.profile_image:
            return static("assets/img/profile.png")
        return self.profile_image.url
