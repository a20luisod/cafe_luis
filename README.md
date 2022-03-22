## Name
cafeLuis

## Description

   Modulo de Odoo simple para la gestion de recursos y productos producidos a partir de esto, orientado a la organización de si ciertas recetas se pueden sacar en una cafetería.


## Installation

   Lo primero es añadir el docker a la lista de modulos de Odoo, añadiendolo a donde apunte su addons paht o modificando este.
   Después buscando el modulo por Cafe en la barra buscadora o bien entrando en la categoría productividad devería aparecerte.
   Se pulsa en instalar y esperas a que se instale.


## Usage

  Una vez instalado en la esquina superior izquieda el menú reperesentado con cuatro cuadrados, prodrás ver que despliega y aparecerá la opcion Cafe.
  
  Una vez en esta ventada tendremos en el menú de la barra superior otros dos desplegables Cofees e Ingredientes. Cada uno te llevara a una funcionalidad.
  
  Ingredientes:
  	-Al clicar en el boton Crear aparecerá un formulario para añadir un ingrediente.
  	-Tendremos que rellenar los datos del ingrediente.
  	-Pulsamos Guardar.
  	-De vuelta en Ingredients podemos ver que hay una lista de los ingredientes añadidos sus campos y como añadido un campo calculado el cual te indica si la fecha de caducidad de un producto ya ha pasado.

     --También posee otra vista Kanban por si esta resulta mas cómoda --
     	--Para acceder a ella Clicar el boton representado con 4 cuadrados el la esquina superior derecha. 
  	
  Cofees:
  	-Al clicar en el boton Crear aparecerá un formulario para añadir un cafes.
  	-Asignamos un nombre y despues al clicar en Añadir Linea apareceran los ingredientes que pueden formar la receta.
  	-Pulsamos Guardar.
  	-De nuevo en Cofees vemos que aparecerá el cafe con el campo "Is cofee avaliable" el cual te indicará que esta disponible siempre y cuando todos los ingredientes que forma un receta estén disponibles tanto por Stock como por Caducidad.
  	

## Roadmap
  
  En futuras actualizaciones me gustatría:
  
   -Hacer que el campo calculado de los cafés no solo te diga que puede hacer hacerlos si no también la cantidad.
   -Que en el modelo de ingredientes heredara de un modelo que ya almacena Stock en el propio Odoo para tenerlo así todo más unificado.


## Authors and acknowledgment
Luis Otero de Andrés

## License
GPL

