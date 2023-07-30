from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def post(requests):
    posts = Post.objects.all()
    return render(requests, 'blog/index.html',{'posts':posts})


def post_detail(request, slug: str):

    detail = get_object_or_404(Post,slug=slug)

    return render(request, 'blog/detail.html', {'detail':detail})
