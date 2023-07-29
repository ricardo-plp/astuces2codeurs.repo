from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify


class Post(models.Model):
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
