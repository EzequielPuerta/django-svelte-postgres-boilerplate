from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest

from api.models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ("id", "file", "uploaded_at", "user", "compressed_content")
    readonly_fields = ("id", "uploaded_at", "user", "compressed_content")

    def save_model(
        self,
        request: HttpRequest,
        obj: UploadedFile,
        form: ModelForm,  # type: ignore[type-arg]
        change: bool,
    ) -> None:
        if not obj.pk:
            obj.user = request.user  # type: ignore[assignment]
        super().save_model(request, obj, form, change)
