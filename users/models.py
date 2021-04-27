from django.db import models
from django.urls import reverse

class User_Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.user.username
