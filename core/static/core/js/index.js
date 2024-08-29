const radioButtons = document.querySelectorAll('input[type=radio][name=tipo]');
const inputDocumento = document.querySelector('input[name=identificacion]');



function validarRut(rut) {
    const regex = /^(\d{1,3})(\d{3})(\d{3})-([\dkK])$/;
    const match = regex.exec(rut);
    if (!match) {
      return false; // El formato del RUT es incorrecto
    }
    const numero = match[1] + match[2] + match[3];
    const digitoVerificador = match[4].toUpperCase();
    const factor = [3, 2, 7, 6, 5, 4, 3, 2];
    let suma = 0;
    for (let i = 0; i < factor.length; i++) {
      suma += parseInt(numero.charAt(i)) * factor[i];
    }
    const resto = suma % 11;
    const dv = 11 - resto;
    if (dv === 11) {
      if (digitoVerificador !== '0') {
        return false; // El dígito verificador es incorrecto
      }
    } else if (dv === 10) {
      if (digitoVerificador !== 'K') {
        return false; // El dígito verificador es incorrecto
      }
    } else {
      if (dv.toString() !== digitoVerificador) {
        return false; // El dígito verificador es incorrecto
      }
    }
    return true;
  }
  
  function actualizarPattern() {
    const tipoSeleccionado = document.querySelector('input[type=radio][name=tipo]:checked').value;
    if (tipoSeleccionado === 'rut') {
      inputDocumento.setAttribute('pattern', '[0-9]{2}\[0-9]{3}\[0-9]{3}-[0-9Kk]{1}');
    } else if (tipoSeleccionado === 'pasaporte') {
      inputDocumento.setAttribute('pattern', '^[A-Za-z]{2}[0-9]{6}[A-Za-z]{1}$');

    }
  }
  
  function validarDocumento() {
    const tipoSeleccionado = document.querySelector('input[type=radio][name=tipo]:checked').value;
    const documento = inputDocumento.value;
    if (tipoSeleccionado === 'rut') {
      if (!validarRut(documento)) {
        inputDocumento.setCustomValidity('RUT inválido');
        return false;
      }
    } else if (tipoSeleccionado === 'pasaporte') {
      const pasaporteRegex = new RegExp('^[A-Za-z]{2}[0-9]{6}[A-Za-z]{1}$');
      if (!pasaporteRegex.test(documento)) {
        inputDocumento.setCustomValidity('Pasaporte inválido');
        return false;
      }
    }
    inputDocumento.setCustomValidity('');
    return true;
  } 
    
    // Ejecutar la función al cargar la página para establecer el pattern inicial
    actualizarPattern();
    
    // Agregar evento "change" a los radio buttons
    radioButtons.forEach(radioButton => {
    radioButton.addEventListener('change', actualizarPattern);
    });
    
    // Agregar evento "input" al campo de texto
    inputDocumento.addEventListener('input', validarDocumento);



$(document).ready(function() {
    // Agregar los mensajes de validación en español a Parsley
    Parsley.addMessages('es', {
      defaultMessage: "Debe seleccionar una Comuna.",
      type: {
        email:        "Este campo debe ser un correo válido.",
        url:          "Este valor debe ser una URL válida.",
        number:       "Este valor debe ser un número válido.",
        integer:      "Este valor debe ser un número válido.",
        digits:       "Este campo debe contener 9 digitos.",
        alphanum:     "Este valor debe ser alfanumérico."
      },
      notblank:       "Este valor no debe estar en blanco.",
      required:       "Este campo es obligatorio.",
      pattern:        "El formato debe ser 12345678-9.",
      min:            "Este valor no debe ser menor que %s.",
      max:            "Este valor no debe ser mayor que %s.",
      range:          "Este valor debe estar entre %s y %s.",
      minlength:      "Este valor es muy corto. La longitud mínima es de %s caracteres.",
      maxlength:      "Este valor es muy largo. La longitud máxima es de %s caracteres.",
      length:         "Este campo debe estar entre %s y %s caracteres.",
      mincheck:       "Debe seleccionar al menos %s opciones.",
      maxcheck:       "Debe seleccionar %s opciones o menos.",
      check:          "Debe seleccionar entre %s y %s opciones."
    });
    Parsley.setLocale('es');
    // Inicializar Parsley en tu formulario y configurar el idioma a español
    $('#formulario').parsley({
      language: 'es' // Establecer el idioma a español
    });
  });

 //////////////////////////////////////////////////////////////////

// Escuchar el evento "submit" del formulario
document.getElementById("formulario").addEventListener("submit", function(event) {
    // Prevenir que el formulario se envíe
    event.preventDefault();
  
    // Capturar los valores de los campos del formulario
    var tipo = document.querySelector('input[name="tipo"]:checked').value;
    var identificacion = document.getElementById("identificacion").value;
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var direccion = document.getElementById("direccion").value;
    var comuna = document.getElementById("comuna").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;
    var marca = document.getElementById("marca").value;
    var año = document.getElementById("año").value;
    var modelo = document.getElementById("modelo").value;
    var servicio = document.getElementById("servicio").value;

   
    if (identificacion === "" || nombre === "" || apellido === "" || direccion === "" || telefono === "" || email === "" || marca === "" || modelo ==="") {
      mensajeError.innerHTML = "Por favor, complete todos los campos";
      
    }else {
      mostrarModal();
  }
    
  
    // Mostrar el modal con los valores capturados
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
    modal.querySelector("#tipo").textContent = tipo;
    modal.querySelector("#identificacion").textContent = identificacion;
    modal.querySelector("#nombre").textContent = nombre;
    modal.querySelector("#apellido").textContent = apellido;
    modal.querySelector("#direccion").textContent = direccion;
    modal.querySelector("#comuna").textContent = comuna;
    modal.querySelector("#telefono").textContent = telefono;
    modal.querySelector("#email").textContent = email;
    modal.querySelector("#marca").textContent = marca;
    modal.querySelector("#año").textContent = año;
    modal.querySelector("#modelo").textContent = modelo;
    modal.querySelector("#servicio").textContent = servicio;
  });
  
  // Selecciona el botón que abre el modal
const botonModal = document.querySelector("#mostrarComprobante");

// Agrega un evento al botón para que al hacer clic muestre el modal con los datos ingresados
botonModal.addEventListener("click", function() {
  // Recupera los valores del formulario
  const tipo = document.querySelector('input[name="tipo"]:checked').value;
  const identificacion = document.querySelector("#identificacion").value;
  const nombre = document.querySelector("#nombre").value;
  const apellido = document.querySelector("#apellido").value;
  const direccion = document.querySelector("#direccion").value;
  const comuna = document.querySelector("#comuna").value;
  const telefono = document.querySelector("#telefono").value;
  const email = document.querySelector("#email").value;
  const marca = document.querySelector("#marca").value;
  const año = document.querySelector("#año").value;
  const modelo = document.querySelector("#modelo").value;
  const servicio = document.querySelector("#servicio").value;

  // Crea el contenido del modal con los datos recuperados
  const modalContenido = `
    <hr></br>
    <h5>Datos Personales</h5>
    <p><strong>Tipo de identificación:</strong> ${tipo}</p>
    <p><strong>Número de identificación:</strong> ${identificacion}</p>
    <p><strong>Nombre:</strong> ${nombre}</p>
    <p><strong>Apellido:</strong> ${apellido}</p>
    <p><strong>Dirección:</strong> ${direccion}</p>
    <p><strong>Comuna:</strong> ${comuna}</p>
    <p><strong>Teléfono:</strong> ${telefono}</p>
    <p><strong>Email:</strong> ${email}</p>
    <br></br>
    <h5>Datos del Vehículo</h5>
    <p><strong>Marca:</strong> ${marca}</p>
    <p><strong>Año:</strong> ${año}</p>
    <p><strong>Modelo:</strong> ${modelo}</p>
    <p><strong>Servicio:</strong> ${servicio}</p>
  `;

  // Selecciona el div que contiene el contenido del modal
  const modalContenedor = document.querySelector("#modal-contenido");

  // Agrega el contenido al div del modal
  modalContenedor.innerHTML = modalContenido;
});

// Obtener el botón de cerrar el modal
var cerrarModal = document.getElementById('cerrar-modal');

// Obtener el botón de cancelar
var cancelarModal = document.getElementById('cancelar-modal');

// Obtener el modal
var modal = document.getElementById('myModal');

// Agregar el evento clic al botón de cerrar
cerrarModal.addEventListener('click', function() {
  // Cerrar el modal manualmente
  modal.style.display = 'none';
});

// Agregar el evento clic al botón de cancelar
cancelarModal.addEventListener('click', function() {
  // Cerrar el modal manualmente
  modal.style.display = 'none';
});

function mostrarAlerta() {
  alert("La información se ha introducido correctamente.")
}

// Funciones para mostrar y ocultar el modal registro exitoso
function mostrarModal() {
  document.getElementById("miModal").style.display = "block";
}
function ocultarModal() {
  document.getElementById("miModal").style.display = "none";
}
