
import json
def recalcular_multimoneda():
    try:
        moneda_de_origen=input("(Ingrese la moneda base (ej. COP, USD, EUR): ")
        moneda_base=input("Ingrese la moneda a la que decea el cambio (ej. COP, USD, EUR): ")
        tasa_de_cambio=float(input("Ingrese la tasa de cambio de la nueva moneda: "))
        if tasa_de_cambio < 0:
              print("Ocurrio un error, ingrese los datos correctamente")
              
        monedas = {
                   "moneda_de_origen":moneda_de_origen,
                   "moneda_base":moneda_base,
                   "tasa_de_cambio":tasa_de_cambio
                        }
        with open("tasas_cambio.json", "w") as archivo_tasasdecambio:
            json.dump(monedas, archivo_tasasdecambio, indent=4)
        print("Cambio de monedas guardado en 'tasas_cambio.json'.")

        while True:
            print("""=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular por fecha
2. Calcular por categoria
3. Regresar al menú principal
=============================================""")

            opcion=input("ingrese la opciona realizar: ")
            if opcion=="1":
                print("""=============================================
          Calcular Total de Gastos
=============================================
Seleccione el periodo de cálculo:

1. Calcular total diario
2. Calcular total semanal
3. Calcular total mensual
4. Regresar al menú principal
=============================================""")
                while True:
                    opcion=input("Ingrese la opcion que desea realizar: ")
                    if opcion=="1":
                        fecha_dia=input("Ingrese la fecha (YYYY-MM-DD): ")

                        with open("informacion_De_Gastos.json","r") as Leer_json:
                            contenido=json.load(Leer_json)
                            total_diario=0
                            for gasto in contenido:
                                fecha_gasto=gasto.get("Fecha","")
                                if fecha_dia == fecha_gasto:
                                    try:
                                        monto=float(gasto.get("Monto del gasto",0))
                                        total_diario+=monto
                                    except ValueError:
                                        print(f"El monto del gasto '{gasto.get('Monto del gasto')}' no es un número válido.")
                            print(f"Total de gastos para el día {fecha_dia} en {moneda_de_origen} : {total_diario}")
                            print(f"Total de gastos para el día {fecha_dia} en {moneda_base}: {total_diario*tasa_de_cambio}")
                            break
                    elif opcion=="2":
                        fecha_inicio=input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                        fecha_fin=input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                        with open("informacion_De_Gastos.json","r") as Leer_json:
                            contenido=json.load(Leer_json)
                            total_semanal=0
                            for gasto in contenido:
                                fecha_gasto=gasto.get("Fecha","")
                                if fecha_inicio <= fecha_gasto <= fecha_fin:
                                    try:
                                        monto=float(gasto.get("Monto del gasto",0))
                                        total_semanal+=monto
                                    except ValueError:
                                        print(f"El monto del gasto '{gasto.get('Monto del gasto')}' no es un número válido.")
                                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {moneda_de_origen} : {total_semanal}")
                                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {moneda_base}: {total_semanal*tasa_de_cambio}")
                                break
                    elif opcion=="3":         
                        fecha_inicio=input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                        fecha_fin=input("Ingrese la fecha de fin (YYYY-MM-DD): ")
                        with open("informacion_De_Gastos.json","r") as Leer_json:
                            contenido=json.load(Leer_json)
                            total_mensual=0
                            for gasto in contenido:
                                fecha_gasto=gasto.get("Fecha","")
                                if fecha_inicio <= fecha_gasto <= fecha_fin:
                                    try:
                                        monto=float(gasto.get("Monto del gasto",0))
                                        total_mensual+=monto
                                    except ValueError:
                                        print(f"El monto del gasto '{gasto.get('Monto del gasto')}' no es un número válido.")
                                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {moneda_de_origen}: {total_mensual}")
                                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {moneda_base}: {total_mensual*tasa_de_cambio}")
                                break
                    elif opcion=="4":
                        break
                    else:
                        print("Opcion no valida, ingrese una opcion correcta")
                        break

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
                                print(gasto*moneda_base)
                                encontrados=True
                        if not encontrados:
                            print(f"No se encontraron gastos en la categoria '{ingresar_categoria}'.")
                        return 
                except FileNotFoundError:
                    print("El archivo no existe.")
                except Exception as e:
                    print(f"OCURRIO UN ERROR {e}.") 
            elif opcion=="3":
                break

                    


    
    except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
    except Exception as e:
                print(f"OCURRIO UN ERROR: {e}")

          

        