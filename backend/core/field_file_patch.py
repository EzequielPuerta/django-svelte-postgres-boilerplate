from django.conf import settings
from django.db.models.fields.files import FieldFile


def custom_url(self: FieldFile) -> str:
    url = self.storage.url(self.name)
    if url.startswith(f"http://django:{settings.BASE_PORT}"):
        url = url.replace(f"http://django:{settings.BASE_PORT}", settings.BASE_URL)
    elif not url.startswith("http"):
        url = f"{settings.BASE_URL}{url}"
    return url


FieldFile.url = property(custom_url)  # type: ignore[assignment]
