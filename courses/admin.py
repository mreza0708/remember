from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Group, Article, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user__email', 'user__name')
    # You could add readonly fields, filters, etc.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('members',)  # Better UI for many-to-many field

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__email', 'author__name')
    list_filter = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'commenter', 'content')
    search_fields = ('article__title', 'commenter__email')
    list_filter = ('article',)
