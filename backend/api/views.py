from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from api.models import UploadedFile
from api.serializers import UploadedFileSerializer


class UploadedFileViewSet(viewsets.ModelViewSet):  # type: ignore[type-arg]
    queryset = UploadedFile.objects.all().order_by("-uploaded_at")
    serializer_class = UploadedFileSerializer
    permission_classes = [DjangoModelPermissions]
