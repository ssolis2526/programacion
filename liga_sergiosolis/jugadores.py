def menu_jugadores(jugadores, equipos):
    opcion = 0
    while opcion != 6:
        print("GESTIÓN DE JUGADORES")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador por ID")
        print("4. Actualizar jugador")
        print("5. Eliminar jugador")
        print("6. Volver")
        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        if opcion == 1:
            crear_jugador(jugadores, equipos)
        elif opcion == 2:
            listar_jugadores(jugadores, equipos)
        elif opcion == 3:
            buscar_jugador(jugadores, equipos)
        elif opcion == 4:
            actualizar_jugador(jugadores, equipos)
        elif opcion == 5:
            eliminar_jugador(jugadores)
        elif opcion == 6:
            break

def crear_jugador(jugadores, equipos):
    if not equipos:
        print("No hay equipos. Crea uno antes.")
        return

    nombre = input("Nombre jugador: ").strip()
    posicion = input("Posición: ").strip()

    print("Equipos disponibles:")
    for e in equipos:
        if e.get("activo", True):
            print(f"{e['id']} - {e['nombre']}")

    try:
        equipo_id = int(input("ID del equipo: "))
    except ValueError:
        print("ID inválido")
        return

    existe = False
    for e in equipos:
        if e["id"] == equipo_id and e.get("activo", True):
            existe = True
    if not existe:
        print("Equipo no válido")
        return

    nuevo_id = len(jugadores) + 1
    jugadores.append({
        "id": nuevo_id,
        "nombre": nombre,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "activo": True
    })
    print("Jugador creado con ID", nuevo_id)

def listar_jugadores(jugadores, equipos):
    print("LISTA DE JUGADORES:")
    encontrado = False
    for j in jugadores:
        if j.get("activo", True):
            encontrado = True
            nombre_equipo = buscar_nombre_equipo(equipos, j.get("equipo_id"))
            print(f"{j['id']} - {j['nombre']} ({j['posicion']}) -> {nombre_equipo}")
    if not encontrado:
        print("(sin jugadores activos)")

def buscar_nombre_equipo(equipos, id_equipo):
    for e in equipos:
        if e["id"] == id_equipo:
            return e["nombre"]
    return "?"

def buscar_jugador(jugadores, equipos):
    try:
        id_buscar = int(input("ID jugador: "))
    except ValueError:
        print("ID inválido")
        return
    for j in jugadores:
        if j["id"] == id_buscar and j.get("activo", True):
            print(j)
            return
    print("No encontrado")

def actualizar_jugador(jugadores, equipos):
    try:
        id_buscar = int(input("ID jugador: "))
    except ValueError:
        print("ID inválido")
        return
    for j in jugadores:
        if j["id"] == id_buscar and j.get("activo", True):
            nuevo_nombre = input("Nuevo nombre (dejar vacío para igual): ").strip()
            nueva_pos = input("Nueva posición (vacío = igual): ").strip()
            nuevo_equipo = input("Nuevo equipo ID (vacío = igual): ").strip()

            if nuevo_nombre != "":
                j["nombre"] = nuevo_nombre
            if nueva_pos != "":
                j["posicion"] = nueva_pos
            if nuevo_equipo != "":
                try:
                    j["equipo_id"] = int(nuevo_equipo)
                except ValueError:
                    print("ID equipo inválido. No se cambia equipo.")

            print("Jugador actualizado")
            return
    print("No encontrado")

def eliminar_jugador(jugadores):
    try:
        id_borrar = int(input("ID jugador: "))
    except ValueError:
        print("ID inválido")
        return
    for j in jugadores:
        if j["id"] == id_borrar:
            j["activo"] = False
            print("Jugador desactivado")
            return
    print("No encontrado")
