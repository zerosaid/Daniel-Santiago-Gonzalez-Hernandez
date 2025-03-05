import os
import json 
import sys
import time
import itertools

def loading_animation(text="Procesando..."):
                animation = itertools.cycle(["🃟","🂠","🃑","🃛","🃜","🃝","🃞","🃁","🃋","🃌","🃍","🃎","🂡","🂫","🂬","🂭","🂮","🂱","🂻","🂼","🂽","🂾", "\\"])
                for _ in range(10):  # Ajusta el rango para cambiar la duración
                    sys.stdout.write(f"\r{text} {next(animation)} ")
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write("\r" + " " * (len(text) + 2) + "\r")  # Borra la línea

def escribir_json(nombre_archivo, diccionario):
    try:
        with open(nombre_archivo,"w", encoding='utf-8') as archivo:
            json.dump(diccionario, archivo, indent=4)
        print(f"Los datos fueron escritos correctamente en el archivo {nombre_archivo}")
    except (KeyError, ValueError) as e:
        print(f"Error al escribir en el archivo {nombre_archivo} : {e}")
    except IOError as e:
        print(f"Ocurrio un error al escribir en el archivo {nombre_archivo} : {e}")

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

def agregar_nuevos_elementos_json(json,new_dicc):
        datos = leer_json(json)
        datos.append(new_dicc)
        escribir_json(json,datos)

def gestion_datos():
    
    loading_animation("Cargando")
    
    nombre =  input("""
    ╔════════════════════════════════════════════════════════════════╗
    ║      Ingrese el nombre del país por ejemplo: Indonesia         ║
    ╚════════════════════════════════════════════════════════════════╝ 
                    """).capitalize()
    
    loading_animation("Cargando")

    codigo_iso =  input("""
    ╔════════════════════════════════════════════════════════════════╗
    ║             Ingrese el código ISO por ejemplo: ID              ║
    ╚════════════════════════════════════════════════════════════════╝
                        """).upper()
    
    loading_animation("Cargando")

    codigo_iso3 =  input("""
    ╔════════════════════════════════════════════════════════════════╗
    ║             Ingrese el código ISO3 por ejemplo: IDN            ║
    ╚════════════════════════════════════════════════════════════════╝                      
                         """).upper()
    loading_animation("Cargando")

    if  nombre in paises:
        print("Pais ya Registrado")
    elif nombre != "" and codigo_iso != "" and codigo_iso3 != "":
        new_dicc = {
                "nombre":nombre,
                "codigo_iso":codigo_iso,
                "codigo_iso3":codigo_iso3 
            }
        if nombre in paises:
            print("Pais ya Registrado")
        agregar_nuevos_elementos_json("paises.json",new_dicc)
        return
    else:
        print("No se ingresaron datos")
    gestion_datos()

def obtener_paises():
    paises = gestion_datos('paises.json')
    return [(p["nombre"], p["codigo_iso"], p["codigo_iso3"]) for p in paises]

def indicadores ():
    loading_animation("Cargando")
    opc= input("""
            ▞▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▚
            ▐  ¿Desea agregar un nuevo indicador? (s/n):  ▌
            ▚▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▞
               """).lower()
    loading_animation("Cargando")
    if opc == "s":
        # Solicita datos al usuario y los guarda en el JSON.
        datos = leer_json("indicadore.json")
        agregar_nuevos_elementos_json("indicadore.json",new_dic)

        nuevo_indicador = {
            "id_indicador": input("Ingrese el ID del indicado, ejemplo: SP.POP.TOTL. ").upper(),
            "descripcion": input("Ingrese la descripción del indicador, ejemplo: Población total. ").capitalize(),
        }
        if any(ind["id_indicador"] == nuevo_indicador["id_indicador"] for ind in datos):
            print("El indicador ya está registrado.")
        else:
            datos.append(nuevo_indicador)
            escribir_json("indicadore.json", datos)
            print("Indicador agregado correctamente.")
    elif opc == "n":
        # Muestra todos los indicadores almacenados en el JSON.
        print("Mostrando indicadores existentes. :P ")
        datos = leer_json("indicadore.json")
        if not datos:
            print("No hay indicadores registrados.")
        else:
            for ind in datos:
                print(f"ID: {ind['id_indicador']}, Descripción: {ind['descripcion']}")

def interaccion_paises():
    loading_animation("Cargando")
    while True:
        opc = input("""
            ⚇☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲⚇
            ╳                                              ╳
            ╳        Digite:                               ╳
            ╳        1. Para ver paises                    ╳
            ╳        2. Para ver o agregar indicadores     ╳
            ╳        3. Para volver                        ╳
            ╳                                              ╳
            ⚇☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲⚇      
                    """)
        loading_animation("Cargando")
        if opc == "1":
            for i in paises:
                loading_animation("Cargando")
                print (i)
        elif opc == "2":
            loading_animation("Cargando")
            indicadores()
        elif opc == "3":
            loading_animation("Cargando")
            return menu()
        else:
            loading_animation("Cargando")
            print("Opción no válida, intente de nuevo.")        

def generar_informe():
    def leer_json(nombre_archivo):
        #Lee y devuelve el contenido del archivo JSON como una lista. Si no existe, crea uno vacío.
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                try:
                    datos = json.load(archivo)
                    return datos if isinstance(datos, list) else []
                except json.JSONDecodeError:
                    return []  # Si hay error en el JSON, devolver lista vacía
        else:
            # Si el archivo no existe, se crea vacío
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4)
            return []

    def guardar_json(nombre_archivo, datos):
        """Guarda los datos en un archivo JSON."""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

    def agregar_dato_poblacion():
        """Permite agregar un nuevo dato de población al JSON."""
        datos = leer_json(NOMBRE_ARCHIVO2)
        loading_animation("Cargando")
        try:
            #Registra los paise si no existe creando un archivo json
            nuevo_dato = {
                "ano": int(input("Ingrese el año del dato: ")),
                "pais": input("Ingrese el nombre del país: ").strip().capitalize(),
                "codigo_iso3": input("Ingrese el código ISO3 del país: ").strip().upper(),
                "indicador_id": "SP.POP.TOTL",
                "descripcion": "Total de población",
                "valor": int(input("Ingrese el valor de la población: ")),
                "estado": "disponible",
                "unidad": "personas"
            }
            datos.append(nuevo_dato)
            guardar_json(NOMBRE_ARCHIVO2, datos)
            loading_animation("Cargando")
            print("\n Nuevo dato agregado correctamente al archivo JSON.")

        except ValueError:
            loading_animation("Cargando")
            print("⚠️ Error: Ingrese valores numéricos en el año y la población.")
    
    #Entrega una lista de los cambiso entre las fechas por los datos ingresados
    def generar_informe():
        loading_animation("Cargando")
        """Genera un informe de población para un país en un período de tiempo específico."""
        datos = leer_json(NOMBRE_ARCHIVO2)

        if not datos:
            loading_animation("Cargando")
            print("No hay datos de población registrados.")
            return

        pais = input("Ingrese el nombre del país: ").strip().capitalize()
        try:
            loading_animation("Cargando")
            anio_inicio = int(input("Ingrese el año de inicio: "))
            anio_fin = int(input("Ingrese el año de fin: "))

            if anio_inicio > anio_fin:
                loading_animation("Cargando")
                print("⚠️ Error: El año de inicio no puede ser mayor que el año de fin.")
                return

            # Filtrar los datos según el país y el período de tiempo
        # (
            datos_filtrados = [
                dato for dato in datos 
                if dato["pais"].capitalize() == pais.capitalize() and anio_inicio <= dato["ano"] <= anio_fin
            ]

            if datos_filtrados:
                loading_animation("Cargando")
                print(f"\n Informe de población para {pais} ({anio_inicio} - {anio_fin}):\n")
                for dato in datos_filtrados:
                    loading_animation("Cargando")
                    print(f"Año: {dato['ano']}, Población: {dato['valor']} {dato['unidad']}")
            else:
                loading_animation("Cargando")
                print(f"⚠️ No se encontraron datos para {pais} en el período {anio_inicio}-{anio_fin}.")
        except ValueError:
            loading_animation("Cargando")
            print("⚠️ Error: Ingrese años válidos en formato numérico.")#) <- La filtracion se da hasta este punto si no hay mas datos esta no se llevara acabo marcando el error :)

    if __name__ == "__main__":
        while True:
            loading_animation("Cargando")
            
            print("""
            ◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛◛
            ▓   1. Agregar un dato de población     ▓
            ▓   2. Generar informe de población     ▓
            ▓   3. Volver a interfaz inicial        ▓
            ◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚◚
                  """)

            opc = input("Seleccione una opción: ")
            if opc == "1":
                loading_animation("Cargando")
                agregar_dato_poblacion()
            elif opc == "2":
                loading_animation("Cargando")
                generar_informe()
            elif opc == "3":
                loading_animation("Te la creiste XD")
                print("Volviendo...")
                return menu()
            else:
                loading_animation("¡¡Oye!!")
                print("⚠️ Opción inválida. Intente de nuevo.")

def modulo_reportes():
    columnas = ['año', 'país', 'población', 'indicador']
    print("Opciones disponibles para filtros:")
    for i, columna in enumerate(columnas, 1):
        print(f"{i}. {columna}")
    
    filtros_seleccionados = {}
    
    while True:
        try:
            num_filtros = int(input("¿Cuántos filtros deseas aplicar? (0-4): "))
            if num_filtros < 0 or num_filtros > 4:
                raise ValueError("Por favor, elige un número entre 0 y 4.")
            break
        except ValueError as e:
            print(e)
    
    for i in range(num_filtros):
        while True:
            try:
                filtro = int(input(f"Selecciona el filtro {i + 1} (1-4): "))
                if filtro < 1 or filtro > 4:
                    raise ValueError("Por favor, elige un número entre 1 y 4.")
                filtro_nombre = columnas[filtro - 1]
                if filtro_nombre in filtros_seleccionados:
                    print(f"El filtro '{filtro_nombre}' ya ha sido seleccionado. Elige otro.")
                    continue
                valor = input(f"Introduce el valor para '{filtro_nombre}': ").strip()
                if filtro_nombre in ['año', 'población']:
                    valor = int(valor) if valor.isdigit() else None
                    if valor is None:
                        print("⚠️ Error: Debes ingresar un número para este filtro.")
                        continue
                filtros_seleccionados[filtro_nombre] = valor
                break
            except ValueError as e:
                print(e)
    
    return filtros_seleccionados

new_dic={}
archivo = "Paises.json"
opciones = {"1": gestion_datos, "2": interaccion_paises, "3": generar_informe, "4": modulo_reportes}
paises = {i["nombre"]:[i["codigo_iso"], i["codigo_iso3"]] for i in leer_json("paises.json")}
NOMBRE_ARCHIVO = "indicadores.json"
NOMBRE_ARCHIVO2 = "poblacion.json"

def menu ():
    while True:
        os.system("cls" if os.name =="nt" else"clear")
        print("""
            🂠  🂡  🂫  🂬  🂭  🂮  🃟 🃟  🂱  🂻  🂼  🂽  🂾  🂠
                    Gestion de datos del IEG
            🂠  🃁  🃋  🃌  🃍  🃎  🃟 🃟  🃑  🃛  🃜  🃝  🃞  🂠
            """)
        print("Ingrese \n1. Ver Gestión de Datos de Población \n2. Ver Interacción con Países y Indicadores \n3. Generar un informe \n4. Ver Módulo de Reportes \n5. Salir")
        opc = input("Ingrese la opción requerida: \n")
        if opc in opciones:
            os.system("cls" if os.name =="nt" else"clear")
            opciones[opc]()
            input("\n Presione enter para continuar")
        elif opc == "5":
            # Llamar a la animación antes de mostrar la salida final
            loading_animation("Cargando")
            print("¡Proceso completado!")

            break
        else:
            print("Lea bien...")
menu()