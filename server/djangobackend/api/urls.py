from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, AuthorViewSet, CommentViewSet


router = DefaultRouter()
router.register('blog', BlogViewSet, basename='blog')
router.register('author', AuthorViewSet, basename='author')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    url('blog/', include(router.urls))
]
