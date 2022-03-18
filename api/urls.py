from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api import RegisterApi, PostCreateApi, LikeCreateApi, PostUpdateApi, LikeUpdateApi

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterApi.as_view()),

    path('create-post', PostCreateApi.as_view()),
    path('post/<int:pk>', PostUpdateApi.as_view()),

    path('create-like', LikeCreateApi.as_view()),
    path('like/<int:pk>', LikeUpdateApi.as_view()),
]
