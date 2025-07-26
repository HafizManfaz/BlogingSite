from django.db import models
from django.utils import timezone
# from django.db.models.functions import Now

# Create your models here.
class Model(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255)
    body  = models.TextField()
    # published = models.DateTimeField(db_default=Now())
    publish = models.DateTimeField(default=timezone.now)    # post publish kb howi
    created = models.DateTimeField(auto_now_add=True)       # Post kab banayi gayi
    updated = models.DateTimeField(auto_now=True)           # Post kab last edit hui

    class Meta:
        ordering = ['-publish']                             # سب سے نئی پوسٹ سب سے اوپر
        indexes = [
            models.index(fields = ['-publish'])
        ],
    def __str__(self):
        return self.title