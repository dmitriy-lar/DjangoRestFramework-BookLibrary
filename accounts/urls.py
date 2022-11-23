from django.urls import path

from .views import (
    register_view,
    login_view, 
    logout_view, 
    UserCreateAPIView,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('api/register/', UserCreateAPIView.as_view(), name='register-view')


]