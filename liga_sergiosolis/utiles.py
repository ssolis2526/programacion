def leer_int(mensaje, minimo=None):
    while True:
        try:
            v = input(mensaje).strip()
            if v == '':
                print("No puede estar vacío.")
                continue
            n = int(v)
            if minimo is not None and n < minimo:
                print(f"Introduce un número >= {minimo}.")
                continue
            return n
        except ValueError:
            print("Introduce un entero válido.")

def leer_texto(mensaje, permitir_vacio=False):
    while True:
        t = input(mensaje).strip()
        if not permitir_vacio and t == '':
            print("No puede estar vacío.")
            continue
        return t
