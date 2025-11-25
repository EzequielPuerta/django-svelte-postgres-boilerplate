import pytest
from django.core.files.base import ContentFile
from django.utils import timezone

from api.models import UploadedFile


@pytest.mark.django_db
def test_uploaded_file_creation(django_user_model) -> None:  # type: ignore[no-untyped-def]
    user = django_user_model.objects.create_user(username="test", password="pass")
    content = b"hello world"
    uploaded_file = UploadedFile.objects.create(
        user=user, file=ContentFile(content, name="hello.txt")
    )

    assert uploaded_file.file.name.startswith("hello")
    assert uploaded_file.uploaded_at is not None
    assert uploaded_file.uploaded_at <= timezone.now()

    uploaded_file.file.open("rb")
    data = uploaded_file.file.read()
    uploaded_file.file.close()
    assert data == content
