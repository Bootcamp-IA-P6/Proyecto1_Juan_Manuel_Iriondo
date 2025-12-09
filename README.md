# 🚕 Proyecto Python: Taxímetro Digital

## 📝 Descripción del Proyecto

Este proyecto consiste en desarrollar un prototipo de taxímetro digital utilizando Python. El objetivo es modernizar el sistema de facturación de los taxis y crear un sistema que calcule las tarifas a cobrar a los clientes de manera precisa y eficiente.

## 📊 Niveles de Implementación

### 🟢 Nivel Esencial

Desarrollar un programa CLI (Interfaz de Línea de Comandos) en Python.

- Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
- Implementar las siguientes funcionalidades básicas:
  - Iniciar un trayecto.
  - Calcular tarifa mientras el taxi está parado (2 céntimos por segundo).
  - Calcular tarifa mientras el taxi está en movimiento (5 céntimos por segundo).
  - Finalizar un trayecto y mostrar el total en euros.
  - Permitir iniciar un nuevo trayecto sin cerrar el programa.

### 🟡 Nivel Medio

- Implementar un sistema de logs para la trazabilidad del código.
- Permitir la configuración de precios para adaptarse a la demanda actual.
- Crear un registro histórico de trayectos pasados en un archivo de texto plano.

### 📢 Explicación
- Este programa usa dos funciones en main.py :
  - **calculate_fare(seconds_stopped, seconds_moving)** función para calcular la tarifa a pagar una vez terminado el viaje.
  Los parámetros seconds_stopped y seconds_moving son 2 contadores que acumulan los segundos que el taxi está parado y en movimiento.
  - **taximeter()**, ésta es la función principal que muestra en la terminal el menu del programa, llama a la función **calculate_fare** para que calcule la tarifa, inicializa las variables que necesita y muestra los mensajes necesarios para el desarrollo del programa.

- El fichero *logs.py* contiene la función **init_log()** que se importa en *main.py* y se usa para iniciar el sistema de logs.
  - Esta función devuelve un *logger* que se usa en *main.py* para ir anotando la trazabilidad en el fichero *app.log* de la carpeta *logs*

- El programa calcula la tarifa total en euros.
  - la tarifa cuando el taxi está parado es de **0.02 €/sg**
  - la tarifa cuando el taxi está en movimiento es de **0.05 €/sg**
  - el fichero *prices.txt* te da la opción de cambiar los precios.

- El fichero *historical.py* contiene la función **num_lin_file(file)** a la que le pasas el nombre de un fichero de texto, se importa en *main.py* y te devuelve el número de líneas de ese fichero que se usa en *main.py* para ir creando un histórico de rutas en el fichero *historical.txt* de la carpeta *historical*

### 🔍 Funcionalidades
  - start : Comienza a calcular el tiempo y el costo del proyecto.
  - move : Comienza a moverse y acumula los segundos en movimiento.
  - stop : Para y acumula los segundos que está parado.
  - finish : Finaliza el cálculo del trayecto y muestra el costo total.
  - exit : Finaliza el programa si no quieres hacer más viajes.
  - Mientras se ejecuta el programa, internamente se genera un sistema de logs para la trazabilidad del código.
  - En el fichero **prices.txt** podemos cambiar los precios para que la aplicación los tenga en cuenta a la hora de hacer los cálculos. Hay que cambiar los precios después del igual.
  - Mientras se ejecuta el programa, internamente se genera un registro histórico de trayectos pasados en un archivo de texto plano.

### 🛠️ Tecnologías Usadas
  - Python

### 💾 Instalación
1.- Clona el repositorio

    git clone https://github.com/Bootcamp-IA-P6/Proyecto1_Juan_Manuel_Iriondo.git

2.- Navega al directorio de proyecto

    cd dir Proyecto1_Juan_Manuel_Iriondo ??????

### 🚀 Uso

1.- Ejecuta el archivo **main.py**

    python main.py

2.- Usa las palabras clave : *start*, *move*, *stop*, *finish* y *exit*. 

### 🪪 Contacto
Si tienes cualquier sugerencia o consulta, contáctame a través de juanmanuel.iriondo@gmail.com



