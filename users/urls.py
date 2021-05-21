from . import views

from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile')
 ]
