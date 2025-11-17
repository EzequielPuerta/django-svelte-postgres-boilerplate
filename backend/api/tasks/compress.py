from celery import shared_task
from django.core.files.storage import default_storage
from loguru import logger

from api.models import UploadedFile
from core.compression import compress_content


@shared_task
def process_uploaded_file(obj_id: str, file_path: str) -> None:
    try:
        obj = UploadedFile.objects.get(id=obj_id)
        with default_storage.open(file_path, "rb") as f:
            content = f.read()
        obj.compressed_content = compress_content(content)
        obj.save(update_fields=["compressed_content"])
        logger.success(
            f"File processed successfully: UploadedFile id={obj_id}, path={file_path}"
        )
    except Exception:
        logger.exception(f"Error processing UploadedFile id={obj_id}, path={file_path}")
        raise
