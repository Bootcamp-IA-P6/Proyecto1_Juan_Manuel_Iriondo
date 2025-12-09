import time

import logs
import prices

def calculate_fare(seconds_stopped, seconds_moving):
    """
    función para calcular la tarifa total en euros.
    - Stopped: depende del valor anotado en price_stopped en el fichero prices.txt €/s
    - Moving: depende del valor anotado en price_moving en el fichero prices.txt €/s
    """
    
    price_moving, price_stopped = prices.read_prices()
    fare = seconds_stopped * price_stopped + seconds_moving * price_moving

    print(f"Este es el total: {fare}")
    return fare

def taximeter():
    """
    Función para manejar y mostrar las opciones del taxímetro.
    """
    print("Welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None  # 'stopped' o 'moving'
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == "start":
            if trip_active:
                print("Error: A trip is already in progress.")
                # Nivel medio LOG
                logger.error('A trip is already in progress.')
                continue

            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Iniciamos en estado 'stopped'
            state_start_time = time.time()
            print("Trip started. Initial state: 'stopped'.")

            # Nivel medio LOG
            logger.info("Trip started. Initial state: 'stopped'.")

        elif command in ("stop", "move"):
            if not trip_active:
                print("Error: No active trip. Please start first.")
                # Nivel medio LOG
                logger.error('No active trip. Please start first.')
                continue

            # Calcula el tiempo del estado anterior
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Cambia el estado
            state = 'stopped' if command == "stop" else 'moving'
            state_start_time = time.time()
            print(f"State changed to '{state}'.")

            # Nivel medio LOG
            logger.info(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_active:
                print("Error: No active trip to finish.")
                # Nivel medio LOG
                logger.error('A trip is already in progress.')
                continue

            # Agrega tiempo del último estado
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Calcula la tarifa total y muestra el resumen del viaje
            total_fare = calculate_fare(stopped_time, moving_time)
            print(f"\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")

            # Nivel medio LOG
            logger.info(f"\n--- Trip Summary ---")
            logger.info(f"Stopped time: {stopped_time:.1f} seconds")
            logger.info(f"Moving time: {moving_time:.1f} seconds")
            logger.info(f"Total fare: € {total_fare:.2f}")
            logger.info("---------------------\n")

            # Reset las variables para el próximo viaje
            trip_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            # Nivel medio LOG
            logger.info('Salida del programa.\n')
            break

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")
            # Nivel medio LOG
            logger.warning('Unknown command. Use: start, stop, move, finish, or exit.')

if __name__ == "__main__":

    # Nivel medio LOG
    #################
    # Crea un logger con la función init_log() para poder escribir los logs en el fichero app.log en la carpeta logs/
    logger = logs.init_log()
    logger.debug('Inicio del LOG.')

    taximeter()
