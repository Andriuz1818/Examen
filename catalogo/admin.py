from django.contrib import admin

# Register your models here.

from .models import Libro, Autor, Categoria, NavItem

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(NavItem)
