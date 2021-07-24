from django.db import models
from posts.models import Post
from users.models import User


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    is_approved = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment


class Reply(models.Model):
    reply = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_replies')
    is_approved = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.reply
