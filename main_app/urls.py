from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles_index, name='articles_index'),
    path('articles/<int:articles_id>/', views.articles_detail, name = 'articles_detail'),
]