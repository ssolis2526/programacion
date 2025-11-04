def menu_equipos(equipos, jugadores):
    opcion = 0
    while opcion != 5:
        print("GESTIÓN DE EQUIPOS")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar por ID")
        print("4. Eliminar equipo")
        print("5. Volver")
        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        if opcion == 1:
            crear_equipo(equipos)
        elif opcion == 2:
            listar_equipos(equipos)
        elif opcion == 3:
            buscar_equipo(equipos)
        elif opcion == 4:
            eliminar_equipo(equipos, jugadores)
        elif opcion == 5:
            break

def crear_equipo(equipos):
    nombre = input("Nombre: ").strip()
    ciudad = input("Ciudad: ").strip()
    if not nombre or not ciudad:
        print("Nombre y ciudad no pueden estar vacíos.")
        return
    nuevo_id = len(equipos) + 1
    equipos.append({"id": nuevo_id, "nombre": nombre, "ciudad": ciudad, "activo": True})
    print("Equipo creado con ID", nuevo_id)

def listar_equipos(equipos):
    print("LISTA DE EQUIPOS:")
    encontrado = False
    for e in equipos:
        if e.get("activo", True):
            encontrado = True
            print(f"{e['id']} - {e['nombre']} ({e['ciudad']})")
    if not encontrado:
        print("(sin equipos activos)")

def buscar_equipo(equipos):
    try:
        id_buscar = int(input("ID: "))
    except ValueError:
        print("ID inválido")
        return
    for e in equipos:
        if e["id"] == id_buscar and e.get("activo", True):
            print(e)
            return
    print("No encontrado")

def eliminar_equipo(equipos, jugadores):
    try:
        id_borrar = int(input("ID: "))
    except ValueError:
        print("ID inválido")
        return
    for j in jugadores:
        if j.get("equipo_id") == id_borrar and j.get("activo", True):
            print("No se puede borrar: tiene jugadores activos")
            return
    for e in equipos:
        if e["id"] == id_borrar:
            e["activo"] = False
            print("Equipo desactivado")
            return
    print("No encontrado")
