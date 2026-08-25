from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null = True
    )

    def __str__(self) -> str:
        return self.title