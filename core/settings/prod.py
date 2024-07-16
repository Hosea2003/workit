from .settings import *

HOST = os.getenv("HOST")

DEBUG = False

ALLOWED_HOSTS = ["localhost", HOST]

CSRF_TRUSTED_ORIGINS = [
    f"http://{HOST}",
    "http://localhost",
]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
