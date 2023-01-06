from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('', views.home , name='home'),
    path('article', views.article , name='article'),
    path('catergory', views.catergory , name='catergory'),
    path('about', views.about, name='about'),
    path('docs', views.docs, name='docs'),

]
