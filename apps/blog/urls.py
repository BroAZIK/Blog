from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name="post_edit"),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]