from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupsViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)
router.register(
    r'groups',
    GroupsViewSet,
    basename='groups'
)

router.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
