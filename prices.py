def get_price(lin):
    """
    Docstring for get_price
    
    :param lin: función a la que se le pasa la línea leída del fichero prices.txt y devuelve la key (concepto) y el precio.
    """
    key = ""
    value = 0

    try:
        indice = lin.index("=")
        words = lin.split('=') 

        key = words[0].strip()
        value = float(words[1].strip())

    except ValueError:
        print("No se encontró el = en la línea ", lin)

    return key, value

def read_prices():
    """
    Docstring for read_prices

    Función que lee línea a línea el fichero prices.txt
    """
    mov = 0.05
    stop = 0.02

    with open("prices.txt", "r") as f:
        for lin in f:
            key, value = get_price(lin.rstrip())

            if key == "price_moving":
                mov = value
            elif key == "price_stopped":
                stop = value


    return mov, stop