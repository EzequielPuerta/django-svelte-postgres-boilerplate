import os
from typing import Any

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def validate_file_size(file) -> None:  # type: ignore[no-untyped-def]
    if file.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(
            f"El archivo no puede superar {settings.MAX_UPLOAD_SIZE / (1024*1024)} MB"
        )


def upload_to(instance, filename) -> Any:  # type: ignore[no-untyped-def]
    return os.path.join(filename)


class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to, validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_files",
    )
    compressed_content = models.TextField(blank=True, null=True, editable=False)

    def __str__(self) -> str:
        return (
            f"{self.file.name} uploaded by {self.user.username} at {self.uploaded_at}"
        )
