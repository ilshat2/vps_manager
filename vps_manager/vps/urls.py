
from rest_framework.routers import DefaultRouter
from .views import VPSViewSet


router = DefaultRouter()
router.register(r'', VPSViewSet)  # Корневой маршрут для API

urlpatterns = router.urls
