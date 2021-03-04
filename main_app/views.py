from django.shortcuts import render, redirect
from .models import Article, Comment
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
  return render(request,'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def articles_index(request):
  articles = request.user.article_set.all()
  return render(request, 'articles/index.html', { 'articles': articles })

@login_required
def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  comment_form = CommentForm()
  return render(request, 'articles/detail.html', {'article': article, 'comment_form': comment_form})

@login_required
def add_comment(request, article_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.article_id = article_id
    new_comment.save()
  return redirect('articles_detail', article_id = article_id)

@login_required
def delete_comment(request, article_id, comment_id):
  new_comment = Comment.objects.get(id=comment_id)
  new_comment.article_id = article_id
  new_comment.delete()
  # form = CommentForm(request.POST)
  # if request.method == 'POST':
  #   new_comment

  return redirect('articles_detail', article_id = article_id)


class CreateArticle(LoginRequiredMixin, CreateView):
  model = Article
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
  model = Article
  fields = ['content']

class ArticleDelete(LoginRequiredMixin, DeleteView):
  model = Article
  success_url='/articles/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('articles_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)