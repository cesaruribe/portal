// Función para mostrar imagen en el modal 

function showImage(imageUrl, nombre) {
    document.getElementById('modalImage').src = imageUrl;
    document.getElementById('imageModalLabel').textContent = nombre;
}


// Funciones para el formulario de nuevo actor 
function setupImagePreview() {
    const imagenInput = document.getElementById('id_imagen');
    const imagePreview = document.getElementById('imagePreview');
    
    if (imagenInput && imagePreview) {
        imagenInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                // Validación básica del tipo de archivo
                if (!file.type.match('image.*')) {
                    alert('Por favor, seleccione un archivo de imagen válido (JPEG, PNG, GIF)');
                    imagenInput.value = '';
                    return;
                }

                // Validación del tamaño (ejemplo: máximo 2MB)
                if (file.size > 2 * 1024 * 1024) {
                    alert('La imagen es demasiado grande. Tamaño máximo permitido: 2MB');
                    imagenInput.value = '';
                    return;
                }

                const reader = new FileReader();
                
                reader.onload = function(e) {
                    imagePreview.src = e.target.result;
                    console.log('Vista previa actualizada:', e.target.result);
                }
                
                reader.readAsDataURL(file);
            }
        });
    }
}

function setupFormValidation() {
    const form = document.querySelector('.post-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            let isValid = true;
            

            // Validación de fecha (no futura)
            const fechaNacimiento = document.getElementById('id_fecha_nacimiento').value;
            if (fechaNacimiento) {
                const hoy = new Date().toISOString().split('T')[0];
                if (fechaNacimiento > hoy) {
                    alert('La fecha de nacimiento no puede ser futura');
                    isValid = false;
                }
            }

            if (!isValid) {
                event.preventDefault();
            }
        });
    }
}

// Inicialización cuando el DOM está listo
document.addEventListener('DOMContentLoaded', function() {
    console.log('Script de actores cargado correctamente');
    
    // Configurar vista previa de imagen (para formulario de nuevo actor)
    setupImagePreview();
    
    // Configurar validaciones del formulario
    setupFormValidation();

});