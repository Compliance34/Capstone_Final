from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from zellis.models import Post, Comment, Like

# Create your views here.

class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all().order_by('-pub_date')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]