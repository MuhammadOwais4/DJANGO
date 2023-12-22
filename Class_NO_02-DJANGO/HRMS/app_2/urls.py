from rest_framework.routers import DefaultRouter
from .views import PersonModelViewSet

router = DefaultRouter()

router.register(
    "mvs", PersonModelViewSet
)

urlpatterns = router.urls