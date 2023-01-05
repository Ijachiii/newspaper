from django.urls import path
from .views import *

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list")
]