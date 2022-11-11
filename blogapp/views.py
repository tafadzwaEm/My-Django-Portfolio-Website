from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogHomeView(ListView):
    model = Post
    template_name = "blogapp/blog_home.html"
    context_object_name = 'posts'
    ordering = ['-date_time']

class PostDetailView(DetailView):
    model = Post
    template_name = "blogapp/post_detail.html"