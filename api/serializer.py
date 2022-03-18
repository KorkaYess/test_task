from rest_framework import  serializers

from .models import Post, Like, User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            password = validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'description', 'tags']


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Post.objects.all()
    )

    class Meta:
        model = Like
        fields = ['id', 'user', 'value', 'post']
