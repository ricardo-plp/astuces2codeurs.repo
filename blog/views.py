from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from blog.models import Post
from blog.forms import CommentForm
from blog.models import Comment

from blog.models import Category


def post(request, category=None):
    posts = Post.objects.all()
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts':posts,
        'page':page,
        'categories':categories,
        'category':category,
    }
    return render(request, 'blog/index.html',context)

#class Post_Index(generic.ListView):
#    queryset = Post.objects.all()
#    template_name = 'blog/index.html'
#    paginate_by = 2
#    context_object_name = 'posts'


def post_detail(request, slug: str):
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/detail.html',
                  {'detail':post,
                   'comments':comments,
                   'new_comment':new_comment,
                   'comment_form': comment_form
                   })
