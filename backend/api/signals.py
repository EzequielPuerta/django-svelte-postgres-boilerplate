from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import UploadedFile
from api.tasks.compress import process_uploaded_file
from loguru import logger


@receiver(post_save, sender=UploadedFile)
def trigger_compression(sender, instance, created, **kwargs):
    if created:
        logger.debug(f"Dispatching Celery task for UploadedFile id={instance.id} (signal)")
        process_uploaded_file.delay(instance.id, instance.file.name)
