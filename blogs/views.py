from django.shortcuts import render
from django.views.generic import ListView

from .models import Author, Blog


class AuthorList(ListView):
    model = Author
    template_name = 'blog/author_list.html'
    context_object_name = 'author'

class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'