from .base import *  # noqa: F403, F405

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")  # noqa: F405

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")  # noqa: F405

# Production database (PostgreSQL example)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),  # noqa: F405
        "USER": os.getenv("DB_USER"),  # noqa: F405
        "PASSWORD": os.getenv("DB_PASSWORD"),  # noqa: F405
        "HOST": os.getenv("DB_HOST"),  # noqa: F405
        "PORT": os.getenv("DB_PORT", "5432"),  # noqa: F405
    }
}

# Production email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")  # noqa: F405
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # noqa: F405
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # noqa: F405
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)  # noqa: F405
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"  # noqa: F405

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"

# Allauth Configuration for production
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
SOCIALACCOUNT_EMAIL_VERIFICATION = "mandatory"

# CORS settings for production
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")  # noqa: F405
