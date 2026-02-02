from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"

    def ready(self) -> None:
        from django.contrib import admin

        from core.widgets.login_form import CustomAuthForm
        # from core.widgets.password_change_form import CustomAuthPasswordChangeForm

        admin.site.site_header = "Boilerplate"
        admin.site.site_title = "Boilerplate"
        admin.site.index_title = "Bienvenido al Boilerplate"
        admin.site.login_form = CustomAuthForm
        # admin.site.password_change_form = CustomAuthPasswordChangeForm
