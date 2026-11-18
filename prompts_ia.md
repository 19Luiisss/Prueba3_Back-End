# Bitácora de Inteligencia Artificial 

## Prompt 1: Hacer que el catálogo se vea como una tienda real
*   **Rol:** Eres un diseñador web experto en Bootstrap y Django.
*   **Tarea:** Ayúdame a diseñar la grilla de productos de mi catálogo.
*   **Contexto:** Estoy haciendo una tienda deportiva en Django. Ya tengo la vista con los datos, pero la página se ve muy simple y fea, 
todo apilado hacia abajo. Quiero que los productos se vean en tarjetas (cards) de Bootstrap, de esas que tienen la imagen arriba, el título, 
el precio y un botón abajo. Que sea responsivo.
*   **Formato:** Pásame el código HTML usando las clases de Bootstrap 5 (row, col-md-3, card, etc.) asumiendo que estoy usando un bucle `{% for %}` en Django. 

## Prompt 2: Alertas de éxito con Bootstrap y Django
*   **Rol:** Actúa como un Desarrollador Backend Senior.
*   **Tarea:** Implementar mensajes de feedback visual para el usuario.
*   **Contexto:** Ya tengo listo mi `CreateView` y `DeleteView`, pero al crear o eliminar un artículo la página se recarga sin dar ninguna confirmación. Necesito que aparezca una alerta verde de Bootstrap que diga "Artículo creado correctamente" y que pueda ser cerrada por el usuario.
*   **Formato:** Indícame qué mixin de Django debo agregar en mis vistas para enviar el mensaje de éxito. Proporcióname el bloque de código HTML que debo insertar en `base.html` utilizando las clases de Bootstrap `alert-dismissible` y la lógica de `{% if messages %}`.


## Prompt 3: Arreglar el formulario que se ve desordenado
*   **Rol:** Eres un programador experto en Django.
*   **Tarea:** Estilizar los campos de mi formulario de creación.
*   **Contexto:** Cuando voy a crear un nuevo artículo, uso un `ModelForm`, pero cuando imprimo el formulario en el HTML se ven todos los inputs apretados y sin estilo. 
Necesito que los campos tengan las clases de Bootstrap (como `form-control` o `form-select`) pero sin tener que escribir el HTML de cada input a mano, sino desde `forms.py`.
*   **Formato:** Muéstrame el código de la clase `ArticuloForm` usando el diccionario `widgets`, y dame el pedazo de HTML del template para renderizar el formulario con esas clases.


