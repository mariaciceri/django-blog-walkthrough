from django.db import models
from django.contrib.auth.models import User

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="about")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title