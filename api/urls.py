from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListApiView.as_view()),
    path('posts/<int:pk>/', views.PostUpdateView.as_view())
]
