from django.shortcuts import render, redirect

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm

from .serializers import UserCreateSerializer, UserLoginSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password1', '')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('/')
        else:
            context['form'] = form
    else:
        form = CustomUserCreationForm()
        context['form'] = form
    return render(request, 'accounts/register-page.html', context=context)


def login_view(request):
    context = {}
    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        else:
            context['form'] = form
    else:
        form = CustomUserAuthenticationForm()
        context['form'] = form
    return render(request, 'accounts/login-page.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')



# User Api Views
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPIVIew(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


