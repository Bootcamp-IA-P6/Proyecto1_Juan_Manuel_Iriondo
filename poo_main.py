import time
import os
from datetime import datetime

import logs
import prices
import historical

class Trip:
    """
    Esta clase representa un viaje activo, manejando sus estados, tiempos y cálculo de tarifa.
    """
    def __init__(self, logger):
        self.logger = logger
        self.active = False
        self.start_time = None
        self.state = None
        self.state_start_time = None
        self.stopped_time = 0.0
        self.moving_time = 0.0

    def start(self):
        if self.active:
            raise RuntimeError("A trip is already in progress.")

        self.active = True
        self.start_time = time.time()
        self.stopped_time = 0.0
        self.moving_time = 0.0

        # Por defecto comenzamos en "stopped"
        self.state = "stopped"
        self.state_start_time = time.time()

        self.logger.info("Trip started. Initial state: 'stopped'.")

    def _update_state_time(self):
        """Agrega el tiempo transcurrido del estado actual."""
        if not self.active:
            return

        elapsed = time.time() - self.state_start_time

        if self.state == "stopped":
            self.stopped_time += elapsed
        elif self.state == "moving":
            self.moving_time += elapsed

    def change_state(self, new_state: str):
        if not self.active:
            raise RuntimeError("No active trip. Please start first.")

        self._update_state_time()
        self.state = new_state
        self.state_start_time = time.time()
        self.logger.info(f"State changed to '{new_state}'.")

    def finish(self):
        if not self.active:
            raise RuntimeError("No active trip to finish.")

        # Registra el último tramo
        self._update_state_time()

        # Cálculo final de tarifa
        price_moving, price_stopped = prices.read_prices()
        total_fare = (
            self.stopped_time * price_stopped +
            self.moving_time * price_moving
        )

        self.active = False

        return {
            "stopped": self.stopped_time,
            "moving": self.moving_time,
            "fare": total_fare
        }


class TaximeterApp:
    """
    Prepara el flujo de interacción de consola y delega la lógica del viaje.
    """

    def __init__(self, logger, historical_path):
        self.logger = logger
        self.historical_path = historical_path
        self.trip = Trip(logger)

    def log_historical(self, summary: dict):
        """
        Registra un viaje finalizado en el fichero histórico.
        """
        num_lin = historical.num_lin_file(self.historical_path)
        now = datetime.now()

        with open(self.historical_path, "a", encoding="utf-8") as file:
            if num_lin == 0:
                file.write("NUM_VIAJE,STOPPED_TIME/sg,MOVING_TIME/sg,TOTAL_FARE/€,DATE\n")

            file.write(f"{num_lin + 1},{summary['stopped']:.1f},{summary['moving']:.1f},{summary['fare']:.2f},{now}\n")

            # file.write(
            #     f"{num_lin + 1} Trip = "
            #     f"Stopped time: {summary['stopped']:.1f} seconds - "
            #     f"Moving time: {summary['moving']:.1f} seconds - "
            #     f"Total fare: € {summary['fare']:.2f} - Date: {now}\n"
            # )

    def run(self):
        print("Welcome to the F5 Taximeter!")
        print("Available commands: start, stop, move, finish, exit\n")

        trip_active = False
        start_time = 0
        stopped_time = 0
        moving_time = 0
        state = None  # 'stopped' o 'moving'
        state_start_time = 0

        while True:
            command = input("> ").strip().lower()

            try:
                if command == "start":
                    self.trip.start()
                    print("Trip started. Initial state: 'stopped'.")

                elif command == "stop":
                    self.trip.change_state("stopped")
                    print("State changed to 'stopped'.")

                elif command == "move":
                    self.trip.change_state("moving")
                    print("State changed to 'moving'.")

                elif command == "finish":
                    summary = self.trip.finish()

                    print("\n--- Trip Summary ---")
                    print(f"Stopped time: {summary['stopped']:.1f} seconds")
                    print(f"Moving time: {summary['moving']:.1f} seconds")
                    print(f"Total fare: €{summary['fare']:.2f}")
                    print("---------------------\n")

                    self.logger.info("--- Trip Summary ---")
                    self.logger.info(f"Stopped: {summary['stopped']:.1f}s")
                    self.logger.info(f"Moving:  {summary['moving']:.1f}s")
                    self.logger.info(f"Total:   €{summary['fare']:.2f}")

                    self.log_historical(summary)

                elif command == "exit":
                    print("Exiting the program. Goodbye!")
                    self.logger.info("Program terminated.")
                    break

                else:
                    print("Unknown command. Use: start, stop, move, finish, or exit.")
                    self.logger.warning("Unknown command received.")

            except RuntimeError as e:
                print(f"Error: {e}")
                self.logger.error(str(e))
    

if __name__ == "__main__":
    # Inicialización del logger
    logger = logs.init_log()
    logger.debug("LOG started.")

    # Preparación del archivo histórico
    historical_file = "historical.csv"
    historical_path = os.path.join("historical", historical_file)
    os.makedirs(os.path.dirname(historical_path), exist_ok=True)
    open(historical_path, "a", encoding="utf-8").close()

    # Ejecución de la app
    TaximeterApp(logger, historical_path).run()


    # fecha = "2025-12-12 10:53:50.609651"
    # #fecha = datetime.now()
    # print("fecha antes -> ", fecha)

    # formato = "%Y-%m-%d %H:%M:%S.%f"
    # fecha2 = datetime.strptime(fecha, formato)
    # print("fecha despues -> ", fecha2)