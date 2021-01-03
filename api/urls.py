from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        )

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


urlpatterns = [
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    ]

router = DefaultRouter()
router.register(
    'posts',
    PostViewSet,
    basename='posts'
)

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

router.register(
    'group',
    GroupViewSet,
    basename='group'
)

router.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

token_url = [
    TokenObtainPairView.as_view(),
    TokenRefreshView.as_view()
]

urlpatterns += [
    path('v1/', include(router.urls)),
]
