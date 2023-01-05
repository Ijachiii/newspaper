from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "article_list"