from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import Article, Comment

def articles_with_comments(request):
    comments_qs = Comment.objects.select_related('commenter', 'commenter__profile')
    articles = Article.objects.select_related('author', 'author__profile').prefetch_related(
        Prefetch('comments', queryset=comments_qs)
    )

    data = []
    for article in articles:
        data.append({
            'title': article.title,
            'author': article.author.email,
            'author_bio': article.author.profile.bio if hasattr(article.author, 'profile') else '',
            'comments': [
                {
                    'content': comment.content,
                    'commenter': comment.commenter.email,
                    'commenter_bio': comment.commenter.profile.bio if hasattr(comment.commenter, 'profile') else '',
                }
                for comment in article.comments.all()
            ]
        })

    return JsonResponse(data, safe=False)

# این بخش صرفا جهت تسته!!