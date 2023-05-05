function validarFormulario() {
    var nombre = document.forms["formulario"]["nombre"].value;
    var correo = document.forms["formulario"]["correo"].value;
    var fechaVisita = document.forms["formulario"]["fecha-visita"].value;
    
    
    if (nombre == "") {
        alert("Por favor, ingrese su nombre.");
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