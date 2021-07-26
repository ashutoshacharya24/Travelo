from rest_framework import generics, serializers, permissions, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from posts.models import Post
from tags.models import Tag
from posts.serializers import PostSerializer
from decorators.permissions import method_permission_classes


class PostList(APIView):
    def get(self, request):
        print(request.GET)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def add_tags(self, post, tags):
        for tag in tags:
            try:
                existing_tag = Tag.objects.get(name=tag)
                post.tags.add(existing_tag)
            except Tag.DoesNotExist:
                new_tag = Tag(name=tag)
                new_tag.save()
                post.tags.add(new_tag)
        post.save()

    @method_permission_classes((permissions.IsAuthenticated,))
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(user=request.user)
            post.save()
            if 'tags' in request.data:
                tags = request.data['tags']
                self.add_tags(post, tags)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
