import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError


class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre',]
        

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email



class EmailField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(self.validate_email_format)

    def validate_email_format(self, value):
        email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        if not email_regex.match(value):
            raise forms.ValidationError("Ingresa un correo electrónico válido.")  
        

    
class ContactoForm(forms.ModelForm):
    celular = forms.CharField(label="Celular", max_length=9)
    email = EmailField(label="Email")

    class Meta:
        model = Contacto
        fields = ['nombre', 'celular', 'email', 'mensaje']
        widgets = {
            'estado': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['celular'].widget.attrs['oninput'] = 'this.value = this.value.replace(/[^0-9]/g, "");'
        self.fields['celular'].widget.attrs['onkeypress'] = 'return event.charCode >= 48 && event.charCode <= 57;'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        if not re.match(r'^[9|8|7]\d{8}$', celular):
            raise forms.ValidationError("Ingresa un número de celular válido.")
        return celular

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith(('.com', '.cl')):
            raise forms.ValidationError("Ingresa un correo electrónico con un dominio válido.")
        return email
    
class ContactoFormVisible(forms.ModelForm):
    celular = forms.CharField(label="Celular", max_length=9)
    email = EmailField(label="Email")

    class Meta:
        model = Contacto
        fields = ['nombre', 'celular', 'email', 'mensaje', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['celular'].widget.attrs['oninput'] = 'this.value = this.value.replace(/[^0-9]/g, "");'
        self.fields['celular'].widget.attrs['onkeypress'] = 'return event.charCode >= 48 && event.charCode <= 57;'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        if not re.match(r'^[9|8|7]\d{8}$', celular):
            raise forms.ValidationError("Ingresa un número de celular válido.")
        return celular

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith(('.com', '.cl')):
            raise forms.ValidationError("Ingresa un correo electrónico con un dominio válido.")
        return email
    

class MecanicoForm(forms.ModelForm):
    telefono = forms.CharField(max_length=9)
    email = EmailField()

    class Meta:
        model = Mecanico
        fields = ['nombre', 'snombre', 'apellidop', 'apellidom', 'telefono', 'email', 'especialidad', 'imagen']
        widgets = {
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefono'].widget.attrs['oninput'] = 'this.value = this.value.replace(/[^0-9]/g, "");'
        self.fields['telefono'].widget.attrs['onkeypress'] = 'return event.charCode >= 48 && event.charCode <= 57;'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre
    
    def clean_snombre(self):
        snombre = self.cleaned_data['snombre']
        if len(snombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return snombre
    
    def clean_apellidop(self):
        apellidop = self.cleaned_data['apellidop']
        if len(apellidop) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return apellidop
    
    def clean_apellidom(self):
        apellidom = self.cleaned_data['apellidom']
        if len(apellidom) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return apellidom
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not re.match(r'^[9|8|7]\d{8}$', telefono):
            raise forms.ValidationError("Ingresa un número de celular válido. De 9 numeros y que comience con 7,8 o 9.")
        return telefono

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith(('.com', '.cl')):
            raise forms.ValidationError("Ingresa un correo electrónico con un dominio válido.")
        return email

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'mecanico', 'precio', 'imagen']
        widgets = {
            'mecanico': forms.Select(attrs={'class': 'form-control'}),
        }


    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) > 100:
            raise forms.ValidationError("El nombre debe tener hasta 100 caracteres.")
        return descripcion
    

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre
        
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) > 100:
            raise forms.ValidationError("El nombre debe tener hasta 100 caracteres.")
        return descripcion

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre',]

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return nombre
        

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['marca', 'nombre']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control', 'onchange': 'filtrar_modelos()'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 1:
            raise forms.ValidationError("El nombre debe tener al menos 1 caracteres.")
        return nombre


class TipoVehiculoForm(forms.ModelForm):
    class Meta:
        model = TipoVehiculo
        fields = ['nombre',]

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre


def validate_year(value):
    if value < 1980 or value > 2024:
        raise ValidationError('El año debe estar entre 1980 y 2024.')


class VehiculoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False, widget=forms.FileInput)
    
    class Meta:
        model = Automovil
        fields = ['imagen', 'patente', 'marca', 'modelo', 'anio', 'tipo', 'descripcion', 'servicio']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control', 'onchange': 'filtrar_modelos()'}),
            'modelo': forms.Select(attrs={'class': 'form-control', 'disabled': 'true'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener las marcas disponibles
        marcas = Marca.objects.all()
        
        # Crear una lista de opciones de marcas para el campo 'marca'
        choices = [(marca.id, marca.nombre) for marca in marcas]
        
        # Agregar una opción vacía al principio de la lista
        choices.insert(0, ('', 'Seleccione una marca'))
        
        # Asignar las opciones al campo 'marca'
        self.fields['marca'].choices = choices

        # Deshabilitar el campo 'modelo' inicialmente
        self.fields['modelo'].widget.attrs['disabled'] = 'true'

    def clean(self):
        cleaned_data = super().clean()
        marca_id = cleaned_data.get('marca')
        
        if marca_id:
            modelos = Modelo.objects.filter(marca_id=marca_id)
            self.fields['modelo'].queryset = modelos
            self.fields['modelo'].widget.attrs['disabled'] = 'false'
        else:
            self.fields['modelo'].queryset = Modelo.objects.none()
            self.fields['modelo'].widget.attrs['disabled'] = 'true'

    def clean_patente(self):
        patente = self.cleaned_data['patente']
        if len(patente) < 6:
            raise forms.ValidationError("La patente debe tener el formato AA1234.")
        return patente
    
    def clean_anio(self):
        anio = self.cleaned_data['anio']
        if not re.match(r'^(19[8-9]\d|20[0-1]\d|202[0-4])$', anio):
            raise forms.ValidationError("Ingresa un año dentro del rango 1980 hasta 2024.")
        return anio
    
    
    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) > 100:
            raise forms.ValidationError("El nombre debe tener hasta 100 caracteres.")
        return descripcion
            




