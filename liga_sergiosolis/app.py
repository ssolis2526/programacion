import equipos
import jugadores
import calendario
import ranking

equipos_lista = []
jugadores_lista = []
partidos_lista = []

def menu_principal():
    opcion = 0
    while opcion != 5:
        print("LIGA DEPORTIVA AMATEUR")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")
        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        if opcion == 1:
            equipos.menu_equipos(equipos_lista, jugadores_lista)
        elif opcion == 2:
            jugadores.menu_jugadores(jugadores_lista, equipos_lista)
        elif opcion == 3:
            calendario.menu_calendario(partidos_lista, equipos_lista)
        elif opcion == 4:
            ranking.menu_ranking(partidos_lista, equipos_lista)
        elif opcion == 5:
            print("Saliendo del program")
        else:
            print("Opción no válida")

if __name__ == '__main__':
    menu_principal()
