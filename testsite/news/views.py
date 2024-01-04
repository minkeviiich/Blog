from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    model = News   
    template_name = 'news/index.html'
    context_object_name = 'news'
    
    def get_queryset(self):
        return News.objects.filter(in_published=True)
    
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    allow_empty = False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id =self.kwargs['category_id'], in_published=True)
    

class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
    

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')