from django.contrib import admin
from posts.models import Post, PostPhoto
from comments.models import Comment
from likes.models import PostLike


class PostPhotoAdmin(admin.TabularInline):
    model = PostPhoto
    extra = 0


class CommentAdminInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostLikeAdminInline(admin.TabularInline):
    model = PostLike
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'is_public', 'is_favourite', 'like_count', 'comment_count')
    filter_horizontal = ('tags',)

    inlines = [PostPhotoAdmin, CommentAdminInline, PostLikeAdminInline]

    def like_count(self, obj):
        return obj.post_likes.count()

    def comment_count(self, obj):
        return obj.post_comments.count()

    # def get_queryset(self, request):
    #     return super().get_queryset(request).filter(user=request.user)
