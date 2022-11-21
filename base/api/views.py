from django.shortcuts import render
from .models import producto

# Create your views here.

def home(request):
    productoslistados = producto.objects.all()
    return render(request, 'inicio-ejemplo.html', {'producto': productoslistados})