from django.db import models

# Create your models here.

class NavItem(models.Model):
    id_nav = models.AutoField(primary_key=True)
    titulo_nav = models.CharField(max_length=20, blank=False, null=False)
    url = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.titulo_nav

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, blank=False, null=False)
    anio_publicacion = models.CharField(max_length=4, blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  

    def __str__(self):
        return self.titulo

