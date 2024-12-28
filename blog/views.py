from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView): #listview is a class-based view that lists objects

    def post_detail(request, slug):
        """
        Display an individual :model:`blog.Post`.

        **Context**

        ``post``
        An instance of :model:`blog.Post`.

        **Template:**

        :template:`blog/post_detail.html`
        """
        
        queryset = Post.objects.filter(status=1) #queryset is a variable that contains all the objects of the Post model
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'blog/post_detail.html',
            {'post': post},
        )
    
    template_name = "blog/index.html"
    paginate_by = 6