from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    slug = models.SlugField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
    publish = models.DateTimeField(default=timezone.now())
    Author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posted')

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.post.title

