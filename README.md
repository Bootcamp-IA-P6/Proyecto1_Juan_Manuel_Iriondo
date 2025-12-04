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

### Explicación
- Este programa usa dos funciones :
  - **calculate_fare(seconds_stopped, seconds_moving)** función para calcular la tarifa a pagar una vez terminado el viaje.
  Los parámetros seconds_stopped y seconds_moving son 2 contadores que acumulan los segundos que el taxi está parado y en movimiento.
  - **taximeter()**, ésta es la función principal que muestra en la terminal el menu del programa, llama a calculate_fare     para que calcule la tarifa, inicializa las variables que necesita y muestra los mensajes necesarios para el desarrollo del programa.

