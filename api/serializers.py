from rest_framework import serializers
from zellis.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'description', 'pub_date', 'update', 'image')
        model = Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email')
        model = User