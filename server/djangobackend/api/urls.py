from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BlogViewSet, CommentViewSet, ProjectViewSet


router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('blog', BlogViewSet, basename='blog')
router.register('comment', CommentViewSet, basename='comment')
router.register('project', ProjectViewSet, basename='project')

urlpatterns = [
    url('blog/', include(router.urls))
]
