from django.forms import PasswordInput


class PasswordToggleInput(PasswordInput):
    template_name = "widgets/password_toggle.html"

    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        kwargs["render_value"] = True
        super().__init__(*args, **kwargs)
