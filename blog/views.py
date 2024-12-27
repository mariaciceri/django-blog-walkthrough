from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView): #listview is a class-based view that lists objects
    queryset = Post.objects.filter(status=1) #queryset is a variable that contains all the objects of the Post model
    template_name = "blog/index.html"
    paginate_by = 6