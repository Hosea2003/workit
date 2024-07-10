from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["3.129.128.0", "ec2-3-129-128-0.us-east-2.compute.amazonaws.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "workit.sqlite3",
    }
}

CSRF_TRUSTED_ORIGINS = [
    "3.129.128.0",
    "ec2-3-129-128-0.us-east-2.compute.amazonaws.com",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
