from django.shortcuts import render, redirect

from django.contrib.auth import logout, authenticate, login

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm

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