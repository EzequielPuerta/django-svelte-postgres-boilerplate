from django.contrib import admin
from api.models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at', 'user', 'compressed_content')
    readonly_fields = ("id", 'uploaded_at', 'user', 'compressed_content')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)
