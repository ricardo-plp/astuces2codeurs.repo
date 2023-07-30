from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from blog.models import Post
from blog.forms import CommentForm
from blog.models import Comment


class Post_Index(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/index.html'
    paginate_by = 1
    context_object_name = 'posts'


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
