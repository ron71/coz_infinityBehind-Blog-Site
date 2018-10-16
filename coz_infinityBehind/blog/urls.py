from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.urls import path
from blog.models import Post
from blog import views

app_name='blog'

urlpatterns = [
	
    path('', views.blog, name='blogpage'),
    url(r'(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='blog/post.html')),
    path('portfolio',views.portfolio, name='portfolio')
    
]