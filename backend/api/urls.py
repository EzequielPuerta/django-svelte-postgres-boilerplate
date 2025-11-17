from rest_framework.routers import DefaultRouter

from api.views import UploadedFileViewSet

router = DefaultRouter()
router.register(r"uploaded-files", UploadedFileViewSet, basename="uploaded-files")

urlpatterns = router.urls
