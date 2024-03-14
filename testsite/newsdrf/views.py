from django.shortcuts import render
from rest_framework import generics
from news.models import News
from .serializers import NewsdrfSerializer


class NewsdrfAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsdrfSerializer
    # фильтры 
    # сортировка 

class NewsdrfAPIPost(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsdrfSerializer
    

class NewsdrfAPIDelete(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsdrfSerializer
    
    
class NewsdrfAPIDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsdrfSerializer
    