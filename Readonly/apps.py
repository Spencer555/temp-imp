from django.apps import AppConfig


class ReadonlyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Readonly"
