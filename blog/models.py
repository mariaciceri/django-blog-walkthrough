from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True) #slug is a URL-friendly version of the title
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    ) #one-to-many relationship with User. if user is deleted, all posts are deleted
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)