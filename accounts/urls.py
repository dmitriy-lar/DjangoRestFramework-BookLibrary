from django.urls import path

from .views import (
    register_view,
    login_view, 
    logout_view, 
    UserCreateAPIView,
    UserLoginAPIVIew
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api/register/', UserCreateAPIView.as_view(), name='register-view'),
    path('api/login/', UserLoginAPIVIew.as_view(), name='login-view')


]