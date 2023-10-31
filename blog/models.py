from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings
from ckeditor.fields import RichTextField
# settings.AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    options = (('draft', 'DRAFT'), ('published', 'PUBLISHED'))

    #Here we are extending the model manager to get specific queryset easily
    class PostObjects(models.Manager):
        def get_queryset(self):
            queryset = super().get_queryset().filter(status='published')
            return queryset

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='blog_posts')
    brief = models.TextField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')

    published = models.DateTimeField(auto_now_add=timezone.now)
    updated = models.DateTimeField(auto_now=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='published')

    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
