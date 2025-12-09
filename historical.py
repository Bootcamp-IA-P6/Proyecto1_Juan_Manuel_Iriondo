def num_lin_file(file):
    num_lin = 0
    with open(file, "r", encoding="utf-8") as file:
        for linea in file:
            num_lin += 1

    return num_lin