from rest_framework import generics, permissions, mixins
from rest_framework.response import Response

from .models import Post, Like
from .serializer import (
    RegisterSerializer, UserSerializer,
    PostSerializer, LikeSerializer
)


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully. Login to get your token",
        })


class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeCreateApi(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
