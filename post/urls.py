from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import CategoryViewset, TagViewSet, PostViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewset, basename='category')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls))
    
]