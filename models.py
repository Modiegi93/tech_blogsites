#!/usr/bin/python3
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default-timezone.now)
    tags = models.ManyToManyField('Tag')
    categories = models.ManyToManyField('Category')
    featured_image = models.ImageField(upload_to='blog_post_images/',
                                       null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTime(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
