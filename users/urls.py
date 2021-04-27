from . import views

from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup')
    #Add more paths!!!
]
