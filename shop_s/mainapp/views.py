from django.shortcuts import render
from .models import order_material
# Create your views here.

def index (request):
    table = order_material.objects.all()
    return render(request, 'main/index.html', { 'table': table})


def about (request):
    return render(request, 'main/about.html')
