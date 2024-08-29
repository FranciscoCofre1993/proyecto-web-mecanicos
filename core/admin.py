from django.contrib import admin
from .models import *

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'estado')
    readonly_fields = ('fecha',)

admin.site.register(Contacto, ContactoAdmin)


class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Comuna, ComunaAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Marca, MarcaAdmin)


class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca')

admin.site.register(Modelo, ModeloAdmin)

class TipoVehiculoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(TipoVehiculo, TipoVehiculoAdmin)

class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'anio', 'tipo', 'descripcion', 'servicio', 'imagen')

admin.site.register(Automovil, AutomovilAdmin)

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(Especialidad, EspecialidadAdmin)

class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'snombre', 'apellidop', 'apellidom', 'telefono', 'email', 'especialidad', 'imagen')

admin.site.register(Mecanico, MecanicoAdmin)


class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'mecanico', 'precio', 'imagen')

admin.site.register(Servicio, ServicioAdmin)




#python manage.py createsuperuser