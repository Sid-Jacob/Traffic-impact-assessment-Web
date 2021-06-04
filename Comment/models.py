from django.db import models
from Article.models import Article
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, primary_key=True)
