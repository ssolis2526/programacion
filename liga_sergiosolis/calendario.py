def menu_calendario(partidos, equipos):
    opcion = 0
    while opcion != 5:
        print("CALENDARIO DE PARTIDOS")
        print("1. Crear partido")
        print("2. Listar partidos")
        print("3. Registrar resultado")
        print("4. Eliminar partido")
        print("5. Volver")
        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        if opcion == 1:
            crear_partido(partidos, equipos)
        elif opcion == 2:
            listar_partidos(partidos, equipos)
        elif opcion == 3:
            registrar_resultado(partidos)
        elif opcion == 4:
            eliminar_partido(partidos)
        elif opcion == 5:
            break

def crear_partido(partidos, equipos):
    activos = [e for e in equipos if e.get('activo', True)]
    if len(activos) < 2:
        print("Deben existir al menos 2 equipos activos.")
        return

    print("Equipos disponibles:")
    for e in activos:
        print(f"{e['id']} - {e['nombre']}")

    try:
        local = int(input("ID equipo local: "))
        visitante = int(input("ID equipo visitante: "))
    except ValueError:
        print("ID inválido")
        return

    if local == visitante:
        print("Local y visitante no pueden ser el mismo.")
        return

    nuevo_id = len(partidos) + 1
    partidos.append({
        "id": nuevo_id,
        "local_id": local,
        "visitante_id": visitante,
        "goles_local": None,
        "goles_visitante": None,
        "activo": True
    })
    print("Partido creado con ID", nuevo_id)

def listar_partidos(partidos, equipos):
    print("LISTA DE PARTIDOS:")
    encontrado = False
    for p in partidos:
        if p.get('activo', True):
            encontrado = True
            local = buscar_equipo_nombre(equipos, p.get('local_id'))
            visitante = buscar_equipo_nombre(equipos, p.get('visitante_id'))
            marcador = "Pendiente"
            if p.get('goles_local') is not None:
                marcador = f"{p['goles_local']} - {p['goles_visitante']}"
            print(f"{p['id']} | {local} vs {visitante} | {marcador}")
    if not encontrado:
        print("(sin partidos activos)")

def buscar_equipo_nombre(equipos, id_equipo):
    for e in equipos:
        if e['id'] == id_equipo:
            return e['nombre']
    return "?"

def registrar_resultado(partidos):
    try:
        id_partido = int(input("ID del partido: "))
    except ValueError:
        print("ID inválido")
        return
    for p in partidos:
        if p.get('id') == id_partido and p.get('activo', True):
            try:
                p['goles_local'] = int(input("Goles local: "))
                p['goles_visitante'] = int(input("Goles visitante: "))
            except ValueError:
                print("Goles deben ser números enteros.")
                p['goles_local'] = None
                p['goles_visitante'] = None
                return
            print("Resultado registrado")
            return
    print("Partido no encontrado")

def eliminar_partido(partidos):
    try:
        id_borrar = int(input("ID partido: "))
    except ValueError:
        print("ID inválido")
        return
    for p in partidos:
        if p['id'] == id_borrar:
            p['activo'] = False
            print("Partido eliminado (marcado como inactivo)")
            return
    print("No encontrado")
