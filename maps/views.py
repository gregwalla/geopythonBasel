from django.shortcuts import render


def index(request):
    return render(request, 'maps/basel_map.html')