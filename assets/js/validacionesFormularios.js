function validarFormulario() {
    var nombre = document.forms["formulario"]["nombre"].value;
    var correo = document.forms["formulario"]["correo"].value;
    var fechaVisita = document.forms["formulario"]["fecha-visita"].value;
    var apellido = document.forms["formulario"]["apellido"].value;
    var edad =document.forms["formulario"]["edad"].value;
    var localidad =document.forms["formulario"]["localidad"].value;
    var rut = document.forms["formulario"]["rut"].value;
    
    if (nombre == "") {
        alert("Por favor, ingrese su nombre.");
        return false;
    }
    if (apellido == "") {
        alert("Por favor, ingrese su apellido.");
        return false;
    }
    if (localidad == "") {
        alert("Por favor, ingrese su localidad.");
        return false;
    }
    if (rut == "") {
        alert("Por favor, ingrese su rut.");
        return false;
    }
    if (edad == "") {
        alert("Por favor, ingrese su edad.");
        return false;
    }
    if (correo == "") {
        alert("Por favor, ingrese su correo electrónico.");
        return false;
    }
    if (fechaVisita == "") {
        alert("Por favor, seleccione la fecha de llegada.");
        return false;
    }
    return true;
}