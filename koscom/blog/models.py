from django.db import models
from .validators import min_length


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length(3)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

