from rest_framework import routers
from .api import UserBookViewSet

router = routers.DefaultRouter()
router.register('api/user/books', UserBookViewSet, 'user-book')

urlpatterns = router.urls
