from rest_framework import serializers
from posts.models import Post, PostPhoto
from tags.models import Tag
from users.models import User


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'avatar_url')


class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        exclude = ('post',)


class PostSerializer(serializers.ModelSerializer):
    tags = PostTagSerializer(read_only=True, many=True)
    user = PostUserSerializer(read_only=True)
    post_photos = PostPhotoSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Post
        exclude = ('updated_at',)
