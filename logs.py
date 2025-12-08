import logging
import os

def init_log():
    # Obtiene un logger con el nombre del módulo actual. Así puedes tener múltiples loggers por archivo.
    logger = logging.getLogger(__name__)
    
    # Define la ruta del archivo donde se guardarán los logs:
    log_file = 'app.log'
    log_path = os.path.join('logs', log_file)

    # Crea la carpeta logs/ si todavía no existe (evita errores).
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    # Crea un "handler" que enviará los mensajes al archivo.
    file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')

    # Esto indica cómo se verá cada línea del log.
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Conecta el logger a ese archivo.
    logger.addHandler(file_handler)

    # El logger aceptará mensajes de nivel: DEBUG
    logger.setLevel(logging.DEBUG)

    return logger