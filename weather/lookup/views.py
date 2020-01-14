from django.shortcuts import render


def home(request):
    return render(request, 'lookup/home.html', {})


def about(request):
    return render(request, 'lookup/about.html', {})
