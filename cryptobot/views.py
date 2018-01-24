from django.shortcuts import render

from allocator.models import CapitalAvailable


def index(request):
    return render(request, 'index.html')













