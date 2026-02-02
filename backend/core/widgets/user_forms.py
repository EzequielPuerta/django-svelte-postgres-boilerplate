from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from core.widgets.password_input import PasswordToggleInput


class CustomUserCreationForm(UserCreationForm):  # type: ignore[type-arg]
    class Meta(UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = ("username",)

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = PasswordToggleInput()
        self.fields["password2"].widget = PasswordToggleInput()


class CustomUserChangeForm(UserChangeForm):  # type: ignore[type-arg]
    class Meta(UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User
        fields = "__all__"
        exclude = ("usable_password",)

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        if "password" in self.fields:
            self.fields["password"].widget = PasswordToggleInput()
