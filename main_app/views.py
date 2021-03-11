from django.shortcuts import render, redirect
from .models import Article, Comment, Category
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CommentForm, UpdateCommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from .forms import CategoryForm

def home(request):
  # url = 'https://newsapi.org/v2/everything?q={}&apiKey=0fc74fe908d8477487c894869fc5e7b4'
  # if request.method == 'POST':
  #   form = CategoryForm(request.POST)
  #   form.save()
  # form = CategoryForm()

  # # category = 'soccer'
  
  # # r = r['articles']
  # new_category = Category.objects.all()

  # category_data=[]

  # for category in new_category:
  #   r = requests.get(url.format(category)).json()
  # # for i in news_data:
  # # news_data = {
  # #     'title': r['articles'] ,
  # #     'description' : r['articles']['description'] ,
  # #     'content': r['articles']['content'] ,
  # #     'url_to_image': r['articles']['urlToImage'],
  # # }
  
  #   news_data = {
  #       'category': category.name,
  #       'title': r['articles'][0]['title'] ,
  #       'description' : r['articles'][0]['description'] ,
  #       'content': r['articles'][0]['content'] ,
  #       'url_to_image': r['articles'][0]['urlToImage'],
  # }
  #   category_data.append(news_data)


  # context = {'category_data' : category_data, 'form': form}
  return render(request,'home.html')

def about(request):
  
  
  # print(news_data)

  return render(request, 'about.html')

@login_required
def articles_index(request):
  # url = 'https://newsapi.org/v2/everything?q={}&apiKey=0fc74fe908d8477487c894869fc5e7b4'
  # category = 'soccer'
  
  # # r = r['articles']
  # new_category = Category.objects.all()

  # category_data=[]

  # for category in new_category:
  #   r = requests.get(url.format(category)).json()
  # # for i in news_data:
  # # news_data = {
  # #     'title': r['articles'] ,
  # #     'description' : r['articles']['description'] ,
  # #     'content': r['articles']['content'] ,
  # #     'url_to_image': r['articles']['urlToImage'],
  # # }
  
  #   news_data = {
  #       'category': category.name,
  #       'title': r['articles'][0]['title'] ,
  #       'description' : r['articles'][0]['description'] ,
  #       'content': r['articles'][0]['content'] ,
  #       'url_to_image': r['articles'][0]['urlToImage'],
  # }
  #   category_data.append(news_data)


  # context = {'category_data' : category_data}
  articles = request.user.article_set.all()
  
  return render(request, 'articles/index.html', { 'articles': articles})
  # add context into render block

@login_required
def articles_detail(request, article_id):
  article = Article.objects.get(id=article_id)
  comment_form = CommentForm()
  all_comments = Comment.objects.filter(id=article_id)
  return render(request, 'articles/detail.html', {'article': article, 'comment_form': comment_form})

@login_required
def add_comment(request, article_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.article_id = article_id
    # new_comment.update('content')
    new_comment.save()
  return redirect('articles_detail', article_id = article_id)

@login_required
def delete_comment(request, article_id, comment_id):
  new_comment = Comment.objects.get(id=comment_id)
  # new_comment.article_id = article_id
  new_comment.delete()
  # form = CommentForm(request.POST)
  # if request.method == 'POST':
  #   new_comment
  return redirect('articles_detail', article_id = article_id)

@login_required
def update_comment(request, comment_id, article_id):
  # edit_comment = Comment.objects.filter(id=comment_id)
  # edit_comment.update()
  # return redirect('articles_detail', article_id = article_id)
  # object = Comment.objects.get()
  # article = Article.objects.filter(id=article_id)
  
  
  
  edit_form = CommentForm(request.POST)
  if edit_form.is_valid():
    # new_comment.comment_id = comment_id
    new_comment = Comment.objects.get(id=comment_id)
    
    
    new_comment = edit_form.save(commit=False)
    new_comment = Comment.objects.filter(id=comment_id).update(content = str(new_comment.content))
    print(new_comment)
    # new_comment.update()
    
    # print(comment_id)
    # print(new_comment.content)
    # print(new_comment.date)
   
    # new_comment.save()
      
  # else:
  #   form = UpdateCommentForm(instance=object)
    # return redirect('update_comment', article_id = article_id)
  
  return redirect('articles_detail', article_id = article_id)

def edit_comment(request, article_id, comment_id):
  new_comment = Comment.objects.get(id=comment_id)
  edit_form = UpdateCommentForm()
  return redirect('articles_detail', article_id = article_id)

    

class CreateArticle(LoginRequiredMixin, CreateView):
  model = Article
  fields = ['short_title', 'long_title', 'author', 'publication', 'content']


  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
  model = Article
  fields = ['short_title', 'long_title', 'author', 'publication', 'content']

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

  # api key 0fc74fe908d8477487c894869fc5e7b4

  # https://newsapi.org/v2/top-headlines?country=us&apiKey=0fc74fe908d8477487c894869fc5e7b4