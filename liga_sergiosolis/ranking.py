def menu_ranking(partidos, equipos):
    opcion = 0
    while opcion != 3:
        print("RESULTADOS Y CLASIFICACIÓN")
        print("1. Ver clasificación")
        print("2. Ver estadísticas por equipo")
        print("3. Volver")
        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Introduce un número válido.")
            continue

        if opcion == 1:
            mostrar_clasificacion(partidos, equipos)
        elif opcion == 2:
            estadisticas_equipo(partidos, equipos)
        elif opcion == 3:
            break

def mostrar_clasificacion(partidos, equipos):
    tabla = []

    for e in equipos:
        if e.get('activo', True):
            tabla.append({
                "id": e["id"],
                "equipo": e["nombre"],
                "pj": 0, "gf": 0, "gc": 0,
                "pts": 0
            })

    for p in partidos:
        if p.get('goles_local') is not None:
            local = _buscar_por_id(tabla, p.get('local_id'))
            visit = _buscar_por_id(tabla, p.get('visitante_id'))

            if local is None or visit is None:
                continue

            local["pj"] += 1
            visit["pj"] += 1

            local["gf"] += p.get('goles_local', 0)
            local["gc"] += p.get('goles_visitante', 0)

            visit["gf"] += p.get('goles_visitante', 0)
            visit["gc"] += p.get('goles_local', 0)

            if p.get('goles_local',0) > p.get('goles_visitante',0):
                local["pts"] += 3
            elif p.get('goles_local',0) < p.get('goles_visitante',0):
                visit["pts"] += 3
            else:
                local["pts"] += 1
                visit["pts"] += 1

    tabla_ordenada = sorted(tabla, key=lambda x: x["pts"], reverse=True)

    print("CLASIFICACIÓN:")
    print("Equipo | PJ | GF | GC | PTS")
    for t in tabla_ordenada:
        print(f"{t['equipo']} | {t['pj']} | {t['gf']} | {t['gc']} | {t['pts']}")

def _buscar_por_id(tabla, id_equipo):
    for t in tabla:
        if t.get('id') == id_equipo:
            return t
    return None

def estadisticas_equipo(partidos, equipos):
    try:
        id_eq = int(input("ID del equipo: "))
    except ValueError:
        print("ID inválido")
        return
    equipo = None
    for e in equipos:
        if e.get('id') == id_eq:
            equipo = e
            break
    if not equipo:
        print("Equipo no encontrado")
        return

    pj = gf = gc = pts = 0

    for p in partidos:
        if p.get('goles_local') is not None:
            if p.get('local_id') == id_eq:
                pj += 1
                gf += p.get('goles_local',0)
                gc += p.get('goles_visitante',0)
                pts += puntos_partido(p.get('goles_local',0), p.get('goles_visitante',0))
            elif p.get('visitante_id') == id_eq:
                pj += 1
                gf += p.get('goles_visitante',0)
                gc += p.get('goles_local',0)
                pts += puntos_partido(p.get('goles_visitante',0), p.get('goles_local',0))

    print("Estadísticas de", equipo.get('nombre'))
    print("PJ:", pj, "GF:", gf, "GC:", gc, "PTS:", pts)

def puntos_partido(gf, gc):
    if gf > gc: return 3
    if gf == gc: return 1
    return 0
