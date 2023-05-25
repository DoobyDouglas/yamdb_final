from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       GetTokenView, RegistrationView, ReviewViewSet,
                       TitleViewSet, UserViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
    r'/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'users',
    UserViewSet,
    basename='users'
)
v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', RegistrationView.as_view(), name='registration'),
    path('v1/auth/token/', GetTokenView.as_view(), name='token'),
]
