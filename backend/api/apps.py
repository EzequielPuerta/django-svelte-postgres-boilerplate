from django.apps import AppConfig
from django.contrib import admin


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self) -> None:
        import api.signals  # noqa: F401

        admin.site.site_header = "Boilerplate"
        admin.site.site_title = "Boilerplate"
        admin.site.index_title = "Welcome to the boilerplate"
