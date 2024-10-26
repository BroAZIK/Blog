from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
]