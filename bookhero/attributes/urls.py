from rest_framework import routers
from .api import AttributeViewSet

router = routers.DefaultRouter()
router.register('attributes', AttributeViewSet, 'attributes')

urlpatterns = router.urls
