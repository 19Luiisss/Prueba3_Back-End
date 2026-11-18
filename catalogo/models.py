from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='articulos')
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_ingreso = models.DateField()
    en_stock = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"