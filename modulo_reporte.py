import json

def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"⚠️ El archivo '{nombre_archivo}' no fue encontrado. Creándolo vacío...")

        return []
    except json.JSONDecodeError:
        print(f" Error: El archivo '{nombre_archivo}' no tiene formato JSON válido.")
        return []
    except IOError as e:
        print(f" Error al leer el archivo '{nombre_archivo}': {e}")
        return []

def calcular_crecimiento(anterior, actual):
    if anterior is None:
        return "N/A"
    crecimiento = ((actual - anterior) / anterior) * 100
    icono = "⬆️" if crecimiento > 0 else "⬇️"
    return f"{crecimiento:.2f}% {icono}"

def filtrar_poblacion(datos, pais, anios, id_indicador, estado):
    # Se filtra por estado "disponible"
    filtrados = [d for d in datos if d["estado"] == "disponible"]
    
    if pais and pais.lower() != "todos":
        filtrados = [d for d in filtrados if d["pais"].lower() == pais.lower()]
    
    if anios:
        if len(anios) == 1:
            filtrados = [d for d in filtrados if d["ano"] == anios[0]]
        elif len(anios) == 2:
            filtrados = [d for d in filtrados if anios[0] <= d["ano"] <= anios[1]]
    
    if id_indicador and id_indicador.lower() != "todos":
        filtrados = [d for d in filtrados if d["indicador_id"].lower() == id_indicador.lower()]
    
    return filtrados

def generar_reporte_poblacion(datos,pais="todos", anios=[], id_indicador="todos", estado="D"):
 
    datos_filtrados = filtrar_poblacion(datos, pais, anios, id_indicador, estado)
    
    poblacion_por_pais = {}
    for d in datos_filtrados:
        if d["pais"] not in poblacion_por_pais:
            poblacion_por_pais[d["pais"]] = []
        poblacion_por_pais[d["pais"]].append({"ano": d["ano"], "valor": d["valor"]})
    
    resultado = "Población Total:\n"
    resultado += "Pais               Población\n"
    for pais_key, valores in poblacion_por_pais.items():
        total_poblacion = sum(v["valor"] for v in valores)
        resultado += f"{pais_key:<20}{total_poblacion}\n"
    ancho =20
    for pais_key, valores in poblacion_por_pais.items():
        valores.sort(key=lambda x: x["ano"])
        resultado += f"\n{pais_key}\n"
        resultado += f"{'Año'.center(ancho, ' ')}{'Población'.center(ancho, ' ')}{'Crecimiento'.center(ancho, ' ')}\n"
        anterior = None
        for v in valores:
            crecimiento = calcular_crecimiento(anterior, v["valor"])
            resultado += f"{str(v['ano']).center(ancho, ' ')}{str(v['valor']).center(ancho, ' ')}{str(crecimiento).center(ancho, ' ')}\n"
            anterior = v["valor"]
    
    return resultado

def ingreso_de_datos(datos):

    pais = input("Ingrese el país (o 'todos' para todos): ")
    anios_input = input("Ingrese un año o un rango de años (ejemplo: 2010 o 2010,2020): ")
    if anios_input.strip() == "":
        anios = []
    else:
        try:
            # Si hay coma se asume rango, sino, se toma como año único
            if "," in anios_input:
                anios = [int(x.strip()) for x in anios_input.split(",")]
            else:
                anios = [int(anios_input.strip())]
        except Exception as e:
            print("Error al procesar el/los año(s). Se usará la lista vacía.")
            anios = []
    id_indicador = input("Ingrese el id del indicador (o 'todos'): ")
    estado = input("Ingrese el estado (D para disponible, ND para no disponible): ")
    reporte = generar_reporte_poblacion(datos, pais, anios, id_indicador, estado)
    print(reporte)
    return reporte

"""
    pais = input("Por favor diga el país del cual desea ver el módulo de reporte: ").capitalize()
    datos = leer_json("poblacion.json")
    
    while True:
        try:
            loading_animation("Cargando")

            opc = int(input(
        ▞▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▚
        ▐                   Seleccione:                                                                                                ▌
        ▐   1. Obtener todos los datos de población para un país desde 2000 hasta 2023.                                                ▌
        ▐   2. Listar los países con su información de código ISO y código ISO3.                                                       ▌
        ▐   3. Datos de población para el indicador 'SP.POP.TOTL'.                                                                     ▌
        ▐   4. Obtener los datos de población de los últimos 10 años para todos los países.                                            ▌
        ▐   5. Total de población para el país de su elección en el año 2022.                                                          ▌
        ▐   6. Población total registrada antes del año 2000.                                                                          ▌
        ▐   7. Población total registrada después del año 2010.                                                                        ▌
        ▐   8. Porcentaje de crecimiento de la población de cualquier país entre 2010 y 2020.                                          ▌
        ▐   9. Población del país que desee en el año 2023 (si está disponible).                                                       ▌
        ▐   10. Obtener el año con la población más baja para el país seleccionado.                                                    ▌
        ▐   11. Número de registros de población por año.                                                                              ▌
        ▐   12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.                                         ▌
        ▐   13. Listar los años en los que la población del país escogido superó los 1,000 millones.                                   ▌
        ▐   14. Obtener la población total registrada para todos los países en el año 2000.                                            ▌
        ▐   15. Obtener la población menos registrada para el país elegido en los últimos 20 años.                                     ▌
        ▐   16. Promedio de población registrada por año para el país escogido desde 1980 hasta 2020.                                  ▌
        ▐   17. Cantidad de años con datos de población disponibles para el país escogido.                                             ▌
        ▐   18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.                                  ▌
        ▐   19. Población total del país escogido en 2019.                                                                             ▌
        ▐   20. Años en los que la población del país escogido creció más de 1 millón en comparación con el año anterior.              ▌
        ▐   21. Población registrada del país escogido en cada década desde 1960.                                                      ▌
        ▐   22. Población total registrada para todos los países en 2023.                                                              ▌
        ▐   23. Años en los que no hay datos de población disponibles para el país escogido.                                           ▌
        ▐   24. Año con la población más alta registrada para el país escogido.                                                        ▌
        ▐   25. Años con datos de población disponibles para más de 50 países.                                                         ▌
        ▐   0. Salir.                                                                                                                  ▌
        ▚▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▞                    
            ))
            
            if opc == 0:
                loading_animation("Cargando")
                print("Saliendo del módulo de reportes...")
                break
            elif opc == 1:
                loading_animation("Cargando")
                print([d for d in datos if d["pais"] == pais and 2000 <= d["ano"] <= 2023])
            elif opc == 2:
                loading_animation("Cargando")
                print([{ "pais": d["pais"], "codigo_iso3": d["codigo_iso3"] } for d in datos])
            elif opc == 3:
                loading_animation("Cargando")
                print([d for d in datos if d["indicador_id"] == "SP.POP.TOTL"])
            elif opc == 4:
                loading_animation("Cargando")
                print([d for d in datos if d["ano"] >= 2014])
            elif opc == 5:
                loading_animation("Cargando")
                print([d for d in datos if d["pais"] == pais and d["ano"] == 2022])
            elif opc == 6:
                loading_animation("Cargando")
                print([d for d in datos if d["ano"] < 2000])
            elif opc == 7:
                loading_animation("Cargando")
                print([d for d in datos if d["ano"] > 2010])
            elif opc == 8:
                loading_animation("Cargando")
                poblacion_2010 = next((d["valor"] for d in datos if d["pais"] == pais and d["ano"] == 2010), None)
                poblacion_2020 = next((d["valor"] for d in datos if d["pais"] == pais and d["ano"] == 2020), None)
                if poblacion_2010 and poblacion_2020:
                    crecimiento = ((poblacion_2020 - poblacion_2010) / poblacion_2010) * 100
                    print(f"El porcentaje de crecimiento de {pais} entre 2010 y 2020 fue de {crecimiento:.2f}%")
                else:
                    print("Datos insuficientes para calcular el crecimiento.")
            elif opc == 11:
                loading_animation("Cargando")
                conteo = {ano: sum(1 for d in datos if d["ano"] == ano) for ano in range(2000, 2024)}
                print(conteo)
            elif opc == 12:
                loading_animation("Cargando")
                print([d["pais"] for d in datos if 2019 <= d["ano"] <= 2023 and (d["valor"] / datos[d["ano"] - 1]["valor"] - 1) * 100 > 2])
            elif opc == 16:
                loading_animation("Cargando")
                registros = [d["valor"] for d in datos if d["pais"] == pais and 1980 <= d["ano"] <= 2020]
                print(sum(registros) / len(registros) if registros else "No hay datos suficientes.")
            elif opc == 20:
                loading_animation("Cargando")
                crecimientos = [d["ano"] for d in datos if d["pais"] == pais and (d["valor"] - datos[d["ano"] - 1]["valor"]) > 1_000_000]
                print(crecimientos)
            elif opc == 23:
                loading_animation("Cargando")
                print([ano for ano in range(1960, 2024) if not any(d["pais"] == pais and d["ano"] == ano for d in datos)])
            elif opc == 25:
                loading_animation("Cargando")
                print([ano for ano in range(2000, 2024) if sum(1 for d in datos if d["ano"] == ano) > 50])
            else:
                loading_animation("Cargando")
                print("Opción no implementada o inválida.")

        except ValueError:
            print("Error: Ingrese un número válido.")
    """
