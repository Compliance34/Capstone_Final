from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]