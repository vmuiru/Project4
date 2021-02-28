from django.shortcuts import render, redirect
from .models import Article, Comment
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentForm
# Create your views here.

def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

def articles_index(request):
  articles = Article.objects.all()
  return render(request, 'articles/index.html', { 'articles': articles })

def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  comment_form = CommentForm()
  return render(request, 'articles/detail.html', {'article': article, 'comment_form': comment_form})


def add_comment(request, article_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.article_id = article_id
    new_comment.save()
  return redirect('articles_detail', article_id = article_id)

class CreateArticle(CreateView):
  model = Article
  fields = '__all__'

class ArticleUpdate(UpdateView):
  model = Article
  fields = ['content']

class ArticleDelete(DeleteView):
  model = Article
  success_url='/articles/'

  