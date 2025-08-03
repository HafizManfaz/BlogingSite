from django.db import models
from django.utils import timezone
# from django.db.models.functions import Now
from django.conf import settings
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)





# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255,unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='blog_posts')
    body  = models.TextField()
    # published = models.DateTimeField(db_default=Now())
    publish = models.DateTimeField(default=timezone.now)    # post publish kb howi
    created = models.DateTimeField(auto_now_add=True)       # Post kab banayi gayi
    updated = models.DateTimeField(auto_now=True)           # Post kab last edit hui
    status  = models.CharField(max_length=2,choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ['-publish']                             # سب سے نئی پوسٹ سب سے اوپر
        indexes = [
            models.Index(fields = ['-publish']),
        ]
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year,
                  self.publish.month,
                  self.publish.day,
                  self.slug            ])
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexex = models.Index(field=['created'])

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
    