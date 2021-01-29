from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, AuthorViewSet


router = DefaultRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    url('blogs/', include(router.urls))
]
