from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import *


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'posts'  # your own name for the list as a template variable
    queryset = Post.objects.all()  # Get all posts
    template_name = 'parentnello/posts_list.html'  # Specify your own template name/location


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'parentnello/posts_detail.html'  # Specify your own template name/location
