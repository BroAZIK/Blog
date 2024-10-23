from django.urls import path
from .views import BloggDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<int:pk>/', BloggDetailView.as_view(), name='post_detail')
]