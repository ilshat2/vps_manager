from rest_framework.routers import DefaultRouter
from vps.views import VPSViewSet

router = DefaultRouter()
router.register(r'vps', VPSViewSet)

urlpatterns = router.urls
