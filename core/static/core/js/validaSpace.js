
function validarFormulario() {
    var rut = document.getElementById("txtRut").value.trim();
    var nombre = document.getElementById("txtNombre").value.trim();
    var direccion = document.getElementById("txtDireccion").value.trim();
    var email = document.getElementById("txtEmail").value.trim();

    // Si alguno de los campos está vacío después de eliminar los espacios en blanco, muestra un mensaje de error y devuelve false para cancelar el envío del formulario.
    if (rut === "" || nombre === "" || direccion === "" || email === "") {
        alert("Por favor, completa todos los campos.");
        return false;
    }
    // Si todos los campos tienen valores, devuelve true para enviar el formulario.
    return true;
}

function validarBuscadores() {
    var nombreCliente = document.getElementsByName("query_nombre")[0].value.trim();
    var rutCliente = document.getElementsByName("query_rut")[0].value.trim();
  
    if (nombreCliente === "" && rutCliente === "") {
      alert("Por favor, ingresa al menos un término de búsqueda.");
      return false;
    }
    return true;
  }
  