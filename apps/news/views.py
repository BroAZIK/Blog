from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class NewsPageView(ListView):
    model = Post
    template_name = 'news.html'
