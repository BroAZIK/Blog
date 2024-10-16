from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
