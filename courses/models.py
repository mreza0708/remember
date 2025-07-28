from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('users.User', related_name='course_groups')

class Article(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
