from django.urls import path
from .views import BloggDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog')
]