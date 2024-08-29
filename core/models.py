
from django.db import models

# Create your models here.

class Contacto(models.Model):
    ESTADOS = (
        ('Recibido', 'Recibido'),
        ('En_proceso', 'En proceso'),
        ('Solucionado', 'Solucionado'),
    )

    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    mensaje = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Recibido')

    def __str__(self):
        return self.nombre
    

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TipoVehiculo(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre


    
class Mecanico(models.Model):
    nombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30)
    apellidop = models.CharField(max_length=30)
    apellidom = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='mecanicos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Automovil(models.Model):
    patente = models.CharField(max_length=20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    anio = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)

    def __str__(self):
        return self.patente
