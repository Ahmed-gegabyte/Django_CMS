from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to now when created
    def __str__(self):
        return self.title
