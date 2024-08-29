from .carrito.carrito import Carrito
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib import messages



# Create your views here.

def PaginaPrincipal(request):
    
    return render(request, 'core/PaginaPrincipal.html')

def Mecanicos(request):
    mecanicos = Mecanico.objects.all()

    contexto = {'mecanicos': mecanicos}

    return render(request, 'core/Mecanicos.html', contexto)

def EmpleadoElect(request):
    return render(request, 'core/EmpleadoElect.html')

def EmpleadoCaja(request):
    return render(request, 'core/EmpleadoCaja.html')

def EmpleadoSusp(request):
    return render(request, 'core/EmpleadoSusp.html')

def GaleriaCdC(request):
    return render(request, 'core/GaleriaCdC.html')

def GaleriaEA(request):
    return render(request, 'core/GaleriaEA.html')

def GaleriaMG(request):
    return render(request, 'core/GaleriaMG.html')

def GaleriaSyD(request):
    return render(request, 'core/GaleriaSyD.html')

def paraderoAPiFin(request):
    return render(request, 'core/paraderoAPiFin.html')

def comprobante(request):
    return render(request, 'core/Comprobante.html')

def formulario_compra(request):
    carrito = Carrito(request)
    
    # Obtener el valor de 'compra_exitosa' de la sesión y eliminarlo
    compra_exitosa = request.session.pop('compra_exitosa', False)

    return render(request, 'core/Formulario_compra.html', {'carrito': carrito, 'compra_exitosa': compra_exitosa})


def procesar_compra(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de compra
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        metodo_pago = request.POST.get('metodo_pago')

        numero_tarjeta = None
        clave_unica = None
        banco = None
        numero_tarjeta_transferencia = None
        contrasena_transferencia = None

        if metodo_pago == 'tarjeta':
            numero_tarjeta = request.POST.get('numero_tarjeta')
            clave_unica = request.POST.get('clave_unica')
            # Procesar pago con tarjeta
            # ...

        elif metodo_pago == 'transferencia':
            banco = request.POST.get('banco')
            numero_tarjeta_transferencia = request.POST.get('numero_tarjeta_transferencia')
            contrasena_transferencia = request.POST.get('contrasena_transferencia')
            # Procesar pago por transferencia
            # ...

        # Procesar la compra
        # ...

        # Borrar los elementos del carrito
        carrito = Carrito(request)
        carrito.limpiar()

        # Crear el contexto para renderizar la boleta
        contexto = {
            'nombres': nombres,
            'apellidos': apellidos,
            'email': email,
            'metodo_pago': metodo_pago,
            'numero_tarjeta': numero_tarjeta,
            'clave_unica': clave_unica,
            'banco': banco,
            'numero_tarjeta_transferencia': numero_tarjeta_transferencia,
            'contrasena_transferencia': contrasena_transferencia,
            'carrito': carrito,
            'compra_exitosa': True
        }

        # Mostrar mensaje de compra exitosa
        messages.success(request, '¡Compra exitosa!')

        # Renderizar la boleta
        return render(request, 'core/Comprobante.html', contexto)

    else:
        # Si no se envió un formulario de compra, redirigir a la página adecuada
        return redirect('formulario_compra')


@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    carrito = Carrito(request)

    # Procesar la solicitud de agregar un producto al carrito
    if request.method == 'POST':
        servicio_id = request.POST.get('servicio_id')
        servicio = Servicio.objects.get(id=servicio_id)
        carrito.agregar(servicio)

    # Procesar la solicitud de eliminar un producto del carrito
    if request.method == 'POST':
        servicio_id = request.POST.get('servicio_id')
        servicio = Servicio.objects.get(id=servicio_id)
        carrito.eliminar(servicio)

    # Procesar la solicitud de restar la cantidad de un producto en el carrito
    if request.method == 'POST':
        servicio_id = request.POST.get('servicio_id')
        servicio = Servicio.objects.get(id=servicio_id)
        carrito.restar(servicio)

    compra_exitosa = request.session.pop('compra_exitosa', False)

    return render(request, 'core/Servicios.html', {'servicios': servicios, 'carrito': carrito, 'compra_exitosa': compra_exitosa})

def agregar_al_carrito(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id=servicio_id)
    carrito.agregar(servicio)
    return redirect('servicios')

def eliminar_del_carrito(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id=servicio_id)
    carrito.eliminar(servicio)
    return redirect('servicios')

def restar_del_carrito(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id=servicio_id)
    carrito.restar(servicio)
    return redirect('servicios')

def comprar(request):
    # Lógica de compra exitosa
    # ...
    
    # Borrar los elementos del carrito
    carrito = Carrito(request)
    carrito.limpiar()
    
    # Establecer una variable de sesión para indicar que la compra fue exitosa
    request.session['compra_exitosa'] = True
    
    return redirect('servicios')


def form_mod_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    formulario = EspecialidadForm(instance=especialidad)

    if request.method == 'POST':
        formulario = EspecialidadForm(data=request.POST, instance=especialidad)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')

    datos = {
        'formulario': formulario,
        'especialidad': especialidad
    }

    return render(request, 'core/Mod_Especialidad.html', datos)


def form_del_especialidad(request, id):
    especialidad = Especialidad.objects.get(id=id)
    especialidad.delete()

    return redirect(to='crud_admin')


def form_mod_marca(request, id):
    marca = Marca.objects.get(id=id)
    formulario = MarcaForm(instance=marca)

    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')

    datos = {
        'formulario': formulario,
        'marca': marca
    }

    return render(request, 'core/Mod_Marca.html', datos)


def form_del_marca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()

    return redirect(to='crud_admin')


def form_mod_modelo(request, id):
    modelo = Modelo.objects.get(id=id)
    formulario = ModeloForm(instance=modelo)

    if request.method == 'POST':
        formulario = ModeloForm(data=request.POST, instance=modelo)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')

    datos = {
        'formulario': formulario,
        'modelo': modelo
    }

    return render(request, 'core/Mod_Modelo.html', datos)


def form_del_modelo(request, id):
    modelo = Modelo.objects.get(id=id)
    modelo.delete()

    return redirect(to='crud_admin')

def form_mod_tipovehiculo(request, id):
    tipoVehiculo = TipoVehiculo.objects.get(id=id)
    formulario = TipoVehiculoForm(instance=tipoVehiculo)

    if request.method == 'POST':
        formulario = TipoVehiculoForm(data=request.POST, instance=tipoVehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')

    datos = {
        'formulario': formulario,
        'tipoVehiculo': tipoVehiculo
    }

    return render(request, 'core/Mod_TipoVehiculo.html', datos)


def form_del_tipovehiculo(request, id):
    tipoVehiculo = TipoVehiculo.objects.get(id=id)
    tipoVehiculo.delete()

    return redirect(to='crud_admin')


def form_mod_mecanico(request, id):
    mecanico = Mecanico.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = MecanicoForm(request.POST, request.FILES, instance=mecanico)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')
    else:
        formulario = MecanicoForm(instance=mecanico)  
    
    datos = {
        'formulario': formulario,
        'mecanico': mecanico,
        'url_imagen': mecanico.imagen.url if mecanico.imagen else None
    }
    
    return render(request, 'core/Mod_Mecanico.html', datos)


def form_del_mecanico(request, id):
    mecanico = Mecanico.objects.get(id=id)
    mecanico.delete()

    return redirect(to='crud_admin')

def form_mod_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    formulario = ServicioForm(instance=servicio)

    if request.method == 'POST':
        formulario = ServicioForm(request.POST, request.FILES, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            return redirect('crud_admin')

    datos = {
        'formulario': formulario,
        'servicio': servicio
    }

    return render(request, 'core/Mod_Servicio.html', datos)


def form_del_servicio(request, id):
    tipoVehiculo = Servicio.objects.get(id=id)
    tipoVehiculo.delete()

    return redirect(to='crud_admin')


def form_mod_vehiculo(request, id):
    vehiculo = Automovil.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            print(formulario.errors)
            formulario.save()
            return redirect('crud_admin')
    else:
        formulario = VehiculoForm(instance=vehiculo)  
    
    datos = {
        'formulario': formulario,
        'vehiculo': vehiculo,
        'url_imagen': vehiculo.imagen.url if vehiculo.imagen else None
    }
    
    return render(request, 'core/Mod_Vehiculo.html', datos)



def form_del_vehiculo(request, id):
    vehiculo = Automovil.objects.get(id=id)
    vehiculo.delete()

    return redirect(to='crud_admin')


def Contactenos(request):
    mensaje = ''
    mensaje_success = False
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = 'Formulario enviado, pronto nos pondremos en contacto con usted.'
            mensaje_success = True
            form = ContactoForm()  # Crea una nueva instancia del formulario sin datos
    else:
        form = ContactoForm()

    return render(request, 'core/Contacto.html', {'form': form, 'mensaje': mensaje, 'mensaje_success': mensaje_success})


def form_mod_contacto(request, id):
    contacto = Contacto.objects.get(id=id)
    datos = {
        'form' : ContactoFormVisible(instance=contacto)
    }
    if request.method == 'POST':
        formulario = ContactoFormVisible(data=request.POST, instance=contacto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos modificados'
            return redirect(to='crud_admin')

    return render(request, 'core/Mod_contacto.html', datos)

def form_del_contacto(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()

    return redirect(to='crud_admin')



def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('PaginaPrincipal')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


@login_required
def crud_admin(request):
    mecanicos = Mecanico.objects.all()
    servicios = Servicio.objects.all()
    vehiculos = Automovil.objects.all()
    especialidades = Especialidad.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    tipoVehiculos = TipoVehiculo.objects.all()
    contactos = Contacto.objects.all()

    mecanico_form = MecanicoForm()
    servicio_form = ServicioForm()
    vehiculo_form = VehiculoForm()
    especialidad_form = EspecialidadForm()
    marca_form = MarcaForm()
    modelo_form = ModeloForm()
    tipoVehiculo_form = TipoVehiculoForm()
    contactoForm = ContactoForm()

    if request.method == 'POST':
        if 'mecanico_form' in request.POST:
            mecanico_form = MecanicoForm(request.POST, request.FILES)
            if mecanico_form.is_valid():
                mecanico_form.save()
                return redirect('crud_admin')

        elif 'servicio_form' in request.POST:
            servicio_form = ServicioForm(request.POST, request.FILES)
            if servicio_form.is_valid():
                servicio_form.save()
                return redirect('crud_admin')
            
        elif 'vehiculo_form' in request.POST:
            vehiculo_form = VehiculoForm(request.POST, request.FILES)
            if vehiculo_form.is_valid():
                vehiculo_form.save()
                return redirect('crud_admin')
        
        elif 'especialidad_form' in request.POST:
            especialidad_form = EspecialidadForm(request.POST)
            if especialidad_form.is_valid():
                especialidad_form.save()
                return redirect('crud_admin')
            
        elif 'marca_form' in request.POST:
            marca_form = MarcaForm(request.POST)
            if marca_form.is_valid():
                marca_form.save()
                return redirect('crud_admin')
            
        elif 'modelo_form' in request.POST:
            modelo_form = ModeloForm(request.POST)
            if modelo_form.is_valid():
                modelo_form.save()
                return redirect('crud_admin')
            
        elif 'tipoVehiculo_form' in request.POST:
            tipoVehiculo_form = TipoVehiculoForm(request.POST)
            if tipoVehiculo_form.is_valid():
                tipoVehiculo_form.save()
                return redirect('crud_admin')

        elif 'contactoForm' in request.POST:
            contactoForm = ContactoForm(request.POST)
            if contactoForm.is_valid():
                contactoForm.save()
                return redirect('crud_admin')
            

    context = {
        'mecanicos': mecanicos,
        'servicios': servicios,
        'vehiculos': vehiculos,
        'especialidades': especialidades,
        'marcas': marcas,
        'modelos': modelos,
        'tipoVehiculos': tipoVehiculos,
        'contactos': contactos,
      
        'mecanico_form': mecanico_form,
        'servicio_form': servicio_form,
        'vehiculo_form': vehiculo_form,
        'especialidad_form': especialidad_form,
        'marca_form': marca_form,
        'modelo_form': modelo_form,
        'tipoVehiculo_form': tipoVehiculo_form,
        'contactoForm': contactoForm,
       
    }
    return render(request, 'core/crud_admin.html', context)

def obtener_modelos(request):
    marca_id = request.GET.get('marca_id')
    
    if marca_id:
        modelos = Modelo.objects.filter(marca_id=marca_id).values('id', 'nombre')
        return JsonResponse(list(modelos), safe=False)
    
    return JsonResponse([], safe=False)



