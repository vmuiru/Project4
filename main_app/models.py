from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    short_title = models.CharField(max_length=150)
    long_title = models.CharField(max_length=200)
    author = models.CharField('author(s)',   max_length=150)
    publication = models.CharField('published in: ', max_length=150)
    content = models.TextField(max_length=1000)
    # title = models.CharField(max_length=150)
    # author = models.CharField(max_length=150)
    # content = models.TextField(max_length=1000)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_title and self.author

    def get_absolute_url(self):
        return reverse('articles_index')

   

class Comment(models.Model):
    content = models.CharField(max_length=250)
    date = models.DateField('date of comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author)
    
    class Meta:
        ordering = ['-date']

