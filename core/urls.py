from django.urls import path, include
from.views import *
from . import views

urlpatterns = [
    path('', PaginaPrincipal, name='PaginaPrincipal'),
    path('PaginaPrincipal.html', PaginaPrincipal, name='PaginaPrincipal'),
    path('Mecanicos.html', Mecanicos, name='Mecanicos'),
    path('EmpleadoElect.html', EmpleadoElect, name='EmpleadoElect'),
    path('EmpleadoCaja.html', EmpleadoCaja, name='EmpleadoCaja'),
    path('EmpleadoSusp.html', EmpleadoSusp, name='EmpleadoSusp'),
    path('GaleriaCdC.html', GaleriaCdC, name='GaleriaCdC'),
    path('GaleriaEA.html', GaleriaEA, name='GaleriaEA'),
    path('GaleriaMG.html', GaleriaMG, name='GaleriaMG'),
    path('GaleriaSyD.html', GaleriaSyD, name='GaleriaSyD'),
    path('paraderoAPiFin.html', paraderoAPiFin, name='paraderoAPiFin'),
    path('Servicios.html', servicios, name='servicios'),

    path('Contacto.html', Contactenos, name='Contacto'),
    path('Mod_contacto.html/<id>', form_mod_contacto, name='form_mod_contacto'),
    path('form_del_contacto.html/<id>', form_del_contacto, name='form_del_contacto'),
    path('Mod_Especialidad.html/<id>', form_mod_especialidad, name='form_mod_especialidad'),
    path('Del_especialidad.html/<id>', form_del_especialidad, name='form_del_especialidad'),
    path('Mod_Marca.html/<id>', form_mod_marca, name='form_mod_marca'),
    path('Del_marca.html/<id>', form_del_marca, name='form_del_marca'),
    path('Mod_modelo.html/<id>', form_mod_modelo, name='form_mod_modelo'),
    path('Del_modelo.html/<id>', form_del_modelo, name='form_del_modelo'),
    path('Mod_TipoVehiculo.html/<id>', form_mod_tipovehiculo, name='form_mod_tipovehiculo'),
    path('Del_TipoVehiculo.html/<id>', form_del_tipovehiculo, name='form_del_tipovehiculo'),
    path('Mod_Mecanico.html/<id>', form_mod_mecanico, name='form_mod_mecanico'),
    path('Del_Mecanico.html/<id>', form_del_mecanico, name='form_del_mecanico'),
    path('Mod_Servicio.html/<id>', form_mod_servicio, name='form_mod_servicio'),
    path('Del_Servicio.html/<id>', form_del_servicio, name='form_del_servicio'),
    path('Mod_Vehiculo.html/<id>', form_mod_vehiculo, name='form_mod_vehiculo'),
    path('Del_Vehiculo.html/<id>', form_del_vehiculo, name='form_del_vehiculo'),

    path('register', register, name='register'),
    
    path('crud_admin.html', crud_admin, name='crud_admin'),
    path('obtener_modelos/', views.obtener_modelos, name='obtener_modelos'),

    path('agregar_al_carrito/<int:servicio_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:servicio_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('restar_del_carrito/<int:servicio_id>/', restar_del_carrito, name='restar_del_carrito'),

    path('comprar/', comprar, name='comprar'),

    path('compra/', views.formulario_compra, name='formulario_compra'),
    path('procesar-compra/', views.procesar_compra, name='procesar_compra'),

    path('comprobante/', views.comprobante, name='comprobante'),

]
