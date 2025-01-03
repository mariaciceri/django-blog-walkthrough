from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """Stores a single blog post entry related to :model:`auth.User`.
    """
    
    title = models.CharField(max_length=200, unique=True) 
    slug = models.SlugField(max_length=200, unique=True) #slug is a URL-friendly version of the title
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    ) #one-to-many relationship with User. if user is deleted, all posts are deleted
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Title: {self.title} by {self.author}" 


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author} commented {self.content}"