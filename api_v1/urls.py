from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BoardGameViewSet, CategoryViewSet, ReviewViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('games', BoardGameViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
