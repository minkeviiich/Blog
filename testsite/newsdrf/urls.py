"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from newsdrf.views import NewsdrfAPIView, NewsdrfAPIPost, NewsdrfAPIDelete, NewsdrfAPIDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name = "news_drf"

urlpatterns = router.urls + [
    path('/list', NewsdrfAPIView.as_view(), name="news-view"),
    path('/post', NewsdrfAPIPost.as_view(), name="news-post"),
    path('/delete/<int:pk>', NewsdrfAPIDelete.as_view(), name="news-delete"),
    path('/detail/<int:pk>', NewsdrfAPIDetail.as_view(), name="news-detail"),
]

