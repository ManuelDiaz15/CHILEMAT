// Obtener el formulario
var form = document.querySelector('form');

// Agregar un evento de escucha para el envío del formulario
form.addEventListener('submit', function(event) {
    // Obtener los campos del formulario
    var codigo = document.getElementById('txtCodigo');
    var cliente = document.getElementById('my-select');
    var fecha = document.getElementById('datefecha');
    var productos = document.getElementById('txtProductos');
    // Verificar si algún campo está vacío
    if (codigo.value === '' || cliente.value === '' || fecha.value === '' || productos.value === ''|| document.getElementById('my-select') != 'input') {
        // Prevenir el envío del formulario si hay campos vacíos
        event.preventDefault();
        // Mostrar un mensaje de error
        alert('Por favor, complete todos los campos antes de guardar la venta.');
    }
});
