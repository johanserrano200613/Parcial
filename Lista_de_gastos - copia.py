import json
import os
def lista_de_gastos():
    print("""=============================================
                Listar Gastos
=============================================
Seleccione una opción para filtrar los gastos:

1. Ver todos los gastos
2. Filtrar por categoría
3. Filtrar por rango de fechas
4. Regresar al menú principal
=============================================""")
    while True:
        opcion=input("Ingrese la opcion que desea realizar: ")
        if opcion=="1":
            try:
                with open("informacion_De_Gastos.json","r") as Leer_json:
                    contenido=json.load(Leer_json)
                    if contenido:
                        for gasto in contenido:
                            print(gasto)
                    else:
                        print("No se encontraron gastos registrados.")
                    return lista_de_gastos()

            except FileNotFoundError:
                print("El archivo no existe.")
            except Exception as e:
                print(f"OCURRIO UN ERROR {e}.")

        elif opcion=="2":
            try:
                print("""=============================================
Categorias disponibles:
=============================================                                       
-comida
-transporte
-entretenimiento
-otros
=============================================""")
                ingresar_categoria=input("Ingrese la categoria que desea filtrar: ").lower()
                with open("informacion_De_Gastos.json","r") as Leer_json:
                     contenido=json.load(Leer_json)
                     encontrados=False
                     for gasto in contenido:
                        if str(gasto.get("Categoria","")).lower() == ingresar_categoria:
                            print(gasto)
                            encontrados=True
                     if not encontrados:
                        print(f"No se encontraron gastos en la categoria '{ingresar_categoria}'.")
                     return lista_de_gastos()
            except FileNotFoundError:
                print("El archivo no existe.")
            except Exception as e:
                print(f"OCURRIO UN ERROR {e}.")         
        elif opcion=="3":
            try:
                fecha_inicio=input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                fecha_fin=input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                with open("informacion_De_Gastos.json","r") as Leer_json:
                    contenido=json.load(Leer_json)
                    encontrados=False
                    for gasto in contenido:
                        fecha_gasto=gasto.get("Fecha","")
                        if fecha_inicio <= fecha_gasto <= fecha_fin:
                            print(gasto)
                            encontrados=True
                    if not encontrados:
                        print(f"No se encontraron gastos entre las fechas '{fecha_inicio}' y '{fecha_fin}'.")
                    return lista_de_gastos()
            except FileNotFoundError:
                print("El archivo no existe.")
            except Exception as e:
                print(f"OCURRIO UN ERROR {e}.") 


        elif opcion=="4":
            return 
       
             
    