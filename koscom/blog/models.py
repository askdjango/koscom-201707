from django.db import models
from .validators import min_length_3


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

