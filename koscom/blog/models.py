from django.db import models
from .validators import MinLengthValidator


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

