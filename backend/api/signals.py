from typing import Any

from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from loguru import logger

from api.models import UploadedFile
from api.tasks.compress import process_uploaded_file


@receiver(post_save, sender=UploadedFile)
def trigger_compression(
    sender: type[Model],
    instance: UploadedFile,
    created: bool,
    **kwargs: Any,
) -> None:
    if created:
        logger.debug(
            f"Dispatching Celery task for UploadedFile id={instance.id} (signal)"
        )
        process_uploaded_file.delay(instance.id, instance.file.name)
