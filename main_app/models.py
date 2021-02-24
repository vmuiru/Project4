from django.db import models
from datetime import date

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    content = models.TextField(max_length=1000)
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title and self.author

class Comments(models.Model):
    content = models.CharField(max_length=250)
    date = models.DateField('date of comment')

    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)

    def __str__(self):
        return self.date
