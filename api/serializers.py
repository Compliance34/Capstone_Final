from rest_framework import serializers
from zellis.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'name', 'description', 'pub_date', 'update', 'image')
        model = Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', '', '', '')
        model = User