from django.contrib.auth.forms import AuthenticationForm

from core.widgets.password_input import PasswordToggleInput


class CustomAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = PasswordToggleInput()
