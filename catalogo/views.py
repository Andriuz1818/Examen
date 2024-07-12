from django.shortcuts import render

# Create your views here.

from .models import Libro, Autor, Categoria, NavItem

def inicio(request):
    navbar = NavItem.objects.all()
    context = {'navbar': navbar}
    return render(request, 'catalogo/inicio.html', context)

def libros(request):
    navbar = NavItem.objects.all()
    libros = Libro.objects.all()
    context = {'navbar': navbar, 'libros': libros}
    return render(request, 'catalogo/libros.html', context)

def autores(request):
    navbar = NavItem.objects.all()
    autores = Autor.objects.all()
    context = {'navbar': navbar, 'autores': autores}
    return render(request, 'catalogo/autores.html', context)

def categorias(request):
    navbar = NavItem.objects.all()
    categorias = Categoria.objects.all()
    context = {'navbar': navbar, 'categorias': categorias}
    return render(request, 'catalogo/categorias.html', context)
