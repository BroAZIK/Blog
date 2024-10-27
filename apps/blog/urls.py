from django.urls import path
from .views import *

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='new_post'),
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]