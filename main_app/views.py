from django.shortcuts import render
from .models import Article
# Create your views here.

def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

def articles_index(request):
  articles = Article.objects.all()
  return render(request, 'articles/index.html', { 'articles': articles })

def articles_detail(request, articles_id):
  article = Article.objects.get(id=articles_id)
  return render(request, 'articles/detail.html', {'article': article})