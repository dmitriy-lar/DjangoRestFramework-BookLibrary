from django.shortcuts import render


def register_view(requests):
    return render(request, 'accounts/register-page.html')

