from django.urls import path
from .views import articles_with_comments

urlpatterns = [
    path('articles/', articles_with_comments, name='articles_with_comments'),
]
