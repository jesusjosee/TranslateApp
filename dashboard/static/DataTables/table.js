$(document).ready(function() {
    $('#phrase-table').DataTable({
        order: [[3, 'desc']],
        scrollX: true,
        lengthMenu: [5, 10, 25, 50, 100], // Opciones de número de entradas por página
        pageLength: 5, // Mostrar 5 entradas por página por defecto
        language: {
            lengthMenu: "Mostrar _MENU_ entradas por página", // Texto personalizado en español
            info: "Mostrando _START_ a _END_ de _TOTAL_ entradas",
            infoEmpty: "Mostrando 0 a 0 de 0 entradas",
            infoFiltered: "(filtrado de _MAX_ entradas totales)",
            search: "Buscar:",
            paginate: {
                first: "Primero",
                previous: "Anterior",
                next: "Siguiente",
                last: "Último"
            }
        },
        dom: '<"row"<"col-md-6"l><"col-md-6"f>><"table-responsive"t><"row"<"col-md-6"i><"col-md-6"p>>', // Ajustar la disposición de los elementos
        lengthMenu: [[5, 10, 25, 50, 100], [5, 10, 25, 50, 100]], // Definir opciones de longitud de página
        "lengthMenu": [[5, 10, 25, 50, 100, -1], [5, 10, 25, 50, 100, "Todos"]],
        pageLength: 5
    });
});