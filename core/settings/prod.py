from .settings import *

DEBUG = False

ALLOWED_HOSTS = [
    "3.129.128.0",
    "ec2-3-129-128-0.us-east-2.compute.amazonaws.com",
    "localhost",
]

# CSRF_TRUSTED_ORIGINS = [
#     "3.129.128.0",
#     "ec2-3-129-128-0.us-east-2.compute.amazonaws.com",
#     "localhost",
# ]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
