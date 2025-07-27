from django.db import models
from django.utils import timezone
# from django.db.models.functions import Now
from django.conf import settings

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)





# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','Published'
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)
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