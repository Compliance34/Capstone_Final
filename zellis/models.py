from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.author.username

class Comment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=512)


class Like(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(null=True)

