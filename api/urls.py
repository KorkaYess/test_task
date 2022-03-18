from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api import (
    RegisterApi,
    PostCreateApi, PostUpdateApi, PostDeleteApi, PostApi,
    LikeCreateApi, LikeDeleteApi, LikeApi
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register', RegisterApi.as_view()),

    path('create-post', PostCreateApi.as_view()),
    path('posts', PostApi.as_view()),
    path('post/<int:pk>', PostUpdateApi.as_view()),
    path('delete-post/<int:pk>', PostDeleteApi.as_view()),

    path('create-like', LikeCreateApi.as_view()),
    path('likes', LikeApi.as_view()),
    path('delete-like/<int:pk>', LikeDeleteApi.as_view()),
]
