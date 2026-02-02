from django.contrib.auth.forms import PasswordChangeForm

from core.widgets.password_input import PasswordToggleInput


class CustomAuthPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget = PasswordToggleInput()
        self.fields["new_password1"].widget = PasswordToggleInput()
        self.fields["new_password2"].widget = PasswordToggleInput()
