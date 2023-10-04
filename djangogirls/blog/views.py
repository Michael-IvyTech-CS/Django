from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    """Defines the view 'post_list' which displays all blog posts ordered by publication date."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """Defines the view 'post_detail' which displays a single blog post in detail."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    """Defines the view 'post_new' which displays a form for creating a new blog post."""
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
