$(document).ready(function() {
  // Validar campo de nombres
  $('#nombres').on('input', function() {
    var nombres = $(this).val().trim();
    var errorNombres = $('#error_nombres');

    if (nombres.length < 3) {
      errorNombres.show();
    } else {
      errorNombres.hide();
    }
  });

  // Validar campo de apellidos
  $('#apellidos').on('input', function() {
    var apellidos = $(this).val().trim();
    var errorApellidos = $('#error_apellido');

    if (apellidos.length < 3) {
      errorApellidos.show();
    } else {
      errorApellidos.hide();
    }
  });

  // Validar campo de email
  $('#email').on('input', function() {
    var email = $(this).val().trim();
    var errorEmail = $('#error_email');

    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/.test(email)) {
      errorEmail.show();
    } else {
      errorEmail.hide();
    }
  });

  // Validar campo de número de tarjeta
   // Obtener el campo de número de tarjeta y el elemento para mostrar el mensaje de error
   var numeroTarjetaInput = $('#numero_tarjeta');
   var errorNumeroTarjeta = $('#error_numero_tarjeta');
 
   // Agregar el evento 'input' para formatear y validar el número de tarjeta
   numeroTarjetaInput.on('input', function() {
     // Obtener el valor actual del campo de número de tarjeta
     var numeroTarjeta = $(this).val();
 
     // Eliminar cualquier carácter no numérico del valor del campo
     var numeros = numeroTarjeta.replace(/\D/g, '');
 
     // Limitar la entrada a 16 caracteres
     if (numeros.length > 16) {
       numeros = numeros.slice(0, 16);
     }
 
     // Formatear el número de tarjeta en grupos de cuatro dígitos separados por guiones
     var tarjetaFormateada = '';
     for (var i = 0; i < numeros.length; i++) {
       if (i > 0 && i % 4 === 0) {
         tarjetaFormateada += '-';
       }
       tarjetaFormateada += numeros[i];
     }
 
     // Establecer el valor formateado en el campo de número de tarjeta
     numeroTarjetaInput.val(tarjetaFormateada);
 
     // Mostrar o ocultar el mensaje de error
     if (numeros.length !== 16 || !/^\d{16}$/.test(numeros)) {
       errorNumeroTarjeta.show();
     } else {
       errorNumeroTarjeta.hide();
     }
   });
 
   // Validar el formulario al enviar
   $('#formulario-compra').submit(function(e) {
     // Obtener el valor del campo de número de tarjeta sin guiones
     var numeroTarjeta = numeroTarjetaInput.val().replace(/-/g, '');
 
     // Verificar si el número de tarjeta tiene 16 dígitos y si es un número válido
     if (numeroTarjeta.length !== 16 || !/^\d{16}$/.test(numeroTarjeta)) {
       // Mostrar el mensaje de error debajo del campo de número de tarjeta
       errorNumeroTarjeta.show();
       // Detener el envío del formulario
       e.preventDefault();
     }
   });
 });

  // Validar campo de clave única
  $('#clave_unica').on('input', function() {
    var claveUnica = $(this).val().trim();
    var errorClaveUnica = $('#error_clave_unica');

    if (claveUnica.length !== 4 || !/^\d{4}$/.test(claveUnica)) {
      errorClaveUnica.show();
    } else {
      errorClaveUnica.hide();
    }
  });

  // Validar campo de número de tarjeta para transferencia
  // Obtener el campo de número de tarjeta y el elemento para mostrar el mensaje de error
  var numeroTarjetaInput = $('#numero_tarjeta_transferencia');
  var errorNumeroTarjeta = $('#numero_tarjeta_transferencia');

  // Agregar el evento 'input' para formatear y validar el número de tarjeta
  numeroTarjetaInput.on('input', function() {
    // Obtener el valor actual del campo de número de tarjeta
    var numeroTarjeta = $(this).val();

    // Eliminar cualquier carácter no numérico del valor del campo
    var numeros = numeroTarjeta.replace(/\D/g, '');

    // Limitar la entrada a 16 caracteres
    if (numeros.length > 16) {
      numeros = numeros.slice(0, 16);
    }

    // Formatear el número de tarjeta en grupos de cuatro dígitos separados por guiones
    var tarjetaFormateada = '';
    for (var i = 0; i < numeros.length; i++) {
      if (i > 0 && i % 4 === 0) {
        tarjetaFormateada += '-';
      }
      tarjetaFormateada += numeros[i];
    }

    // Establecer el valor formateado en el campo de número de tarjeta
    numeroTarjetaInput.val(tarjetaFormateada);

    // Mostrar o ocultar el mensaje de error
    if (numeros.length !== 16 || !/^\d{16}$/.test(numeros)) {
      errorNumeroTarjeta.show();
    } else {
      errorNumeroTarjeta.hide();
    }
  });

  // Validar campo de contraseña para transferencia
  $('#contrasena_transferencia').on('input', function() {
    var contrasenaTransferencia = $(this).val().trim();
    var errorContrasenaTransferencia = $('#error_contrasena_transferencia');

    if (contrasenaTransferencia.length < 8 || contrasenaTransferencia.length > 12) {
      errorContrasenaTransferencia.show();
    } else {
      errorContrasenaTransferencia.hide();
    }
  });

  // Validar el formulario al enviar
  $('#formulario-compra').submit(function(e) {
    // Validar campo de nombres
    var nombres = $('#nombres').val().trim();
    var errorNombres = $('#error_nombres');
    if (nombres.length < 3) {
      errorNombres.show();
      e.preventDefault();
    }

    // Validar campo de apellidos
    var apellidos = $('#apellidos').val().trim();
    var errorApellidos = $('#error_apellido');
    if (apellidos.length < 3) {
      errorApellidos.show();
      e.preventDefault();
    }

    // Validar campo de email
    var email = $('#email').val().trim();
    var errorEmail = $('#error_email');
    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/.test(email)) {
      errorEmail.show();
      e.preventDefault();
    }

    // Validar campo de número de tarjeta
    var numeroTarjeta = $('#numero_tarjeta').val().replace(/-/g, '').trim();
    var errorNumeroTarjeta = $('#error_numero_tarjeta');
    if (numeroTarjeta.length !== 16 || !/^\d{16}$/.test(numeroTarjeta)) {
      errorNumeroTarjeta.show();
      e.preventDefault();
    }

    // Validar campo de clave única
    var claveUnica = $('#clave_unica').val().trim();
    var errorClaveUnica = $('#error_clave_unica');
    if (claveUnica.length !== 4 || !/^\d{4}$/.test(claveUnica)) {
      errorClaveUnica.show();
      e.preventDefault();
    }

    // Validar campo de número de tarjeta para transferencia
    var numeroTarjetaTransferencia = $('#numero_tarjeta_transferencia').val().trim();
    var errorNumeroTarjetaTransferencia = $('#error_numero_tarjeta_transferencia');
    if (numeroTarjetaTransferencia.length !== 16 || !/^\d{16}$/.test(numeroTarjetaTransferencia)) {
      errorNumeroTarjetaTransferencia.show();
      e.preventDefault();
    }

    // Validar campo de contraseña para transferencia
    var contrasenaTransferencia = $('#contrasena_transferencia').val().trim();
    var errorContrasenaTransferencia = $('#error_contrasena_transferencia');
    if (contrasenaTransferencia.length < 8 || contrasenaTransferencia.length > 12) {
      errorContrasenaTransferencia.show();
      e.preventDefault();
    }

    // Manejar el evento de envío del formulario
  $('#formulario-compra').submit(function(event) {
    // Prevenir el comportamiento predeterminado del formulario
    event.preventDefault();

    // Realizar la solicitud AJAX para enviar el formulario
    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      success: function(response) {
        // Mostrar la alerta de compra exitosa
        alert('¡Compra exitosa!');

        // Redirigir a la página de comprobante
        window.location.href = response.redirect_url; // Reemplaza "response.redirect_url" con la URL correcta de tu página de comprobante
      },
      error: function(xhr, errmsg, err) {
        // Manejar el error de la solicitud AJAX si es necesario
        console.log(xhr.status + ': ' + xhr.responseText);
      }
    });
  });
});
