from rest_framework import routers
from .api import BookViewSet

router = routers.DefaultRouter()
router.register('api/books', BookViewSet, 'books')

urlpatterns = router.urls
