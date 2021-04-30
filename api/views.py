from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import PostSerializer, UserSerializer
from zellis.models import Post, Comment, Like

# Create your views here.

class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
