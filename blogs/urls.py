from django.urls import path

from .views import AuthorList, BlogList


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('blogs/', BlogList.as_view(), name='blog_list'),
]