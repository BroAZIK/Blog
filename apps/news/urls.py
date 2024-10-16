from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsPageView.as_view(), name='news'),
    # path('about/', views.AboutPageView.as_view(), name="about"),
]
