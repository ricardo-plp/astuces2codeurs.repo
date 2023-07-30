from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def post(requests):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 1)
    page = requests.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'page':page,
    }
    return render(requests, 'blog/index.html',context)


def post_detail(request, slug: str):

    detail = get_object_or_404(Post,slug=slug)

    return render(request, 'blog/detail.html', {'detail':detail})
