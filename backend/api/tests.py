import io
import pytest
from django.core.files.base import ContentFile
from api.models import UploadedFile
from django.utils import timezone


@pytest.mark.django_db
def test_uploaded_file_creation():
    content = b"hello world"
    uploaded_file = UploadedFile.objects.create(
        file=ContentFile(content, name="hello.txt")
    )

    assert uploaded_file.file.name.endswith("hello.txt")
    assert uploaded_file.uploaded_at is not None
    assert uploaded_file.uploaded_at <= timezone.now()

    uploaded_file.file.open('rb')
    data = uploaded_file.file.read()
    uploaded_file.file.close()
    assert data == content
