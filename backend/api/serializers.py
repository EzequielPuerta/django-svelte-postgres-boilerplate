from rest_framework import serializers
from api.models import UploadedFile


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at', 'user', 'compressed_content']
        read_only_fields = ['id', 'uploaded_at', 'user', 'compressed_content']
