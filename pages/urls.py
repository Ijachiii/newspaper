from .views import *
from django.urls import path

urlpatterns = [
    path("", ArticleLiatView.as_view(), name="article_list"),
    path("<int:pk>/edit/", ArticleUpdateview.as_view(), name="article_edit"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete")
]