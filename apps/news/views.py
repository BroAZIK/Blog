from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class NewsPageView(ListView):
    model = Post
    template_name = 'news.html'