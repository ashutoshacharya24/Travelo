from django.db import models
from users.models import User
from tags.models import Tag


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    caption = models.CharField(max_length=100)
    location = models.JSONField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_favourite = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    tags = models.ManyToManyField(Tag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.caption


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_photos')
    photo_url = models.URLField()

    def __str__(self) -> str:
        return self.post.caption
