import json
def calcular():
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
                    tasas = load_tasas()
                    base_moneda = get_base_currency(tasas)
                    total_diario=0
                    for gasto in contenido:
                        fecha_gasto=gasto.get("Fecha","")
                        if fecha_dia == fecha_gasto:
                            try:
                                monto=float(gasto.get("Monto del gasto",0))
                                if "Monto_base" in gasto:
                                    total_diario += float(gasto.get("Monto_base", monto))
                                else:
                                    moneda = normalize_currency(gasto.get("Moneda", base_moneda))
                                    convertido = convert_to_base(monto, moneda, base_moneda, tasas)
                                    total_diario += convertido if convertido is not None else monto
                            except ValueError:
                                print(f"El monto del gasto '{gasto.get('Monto del gasto')}' no es un número válido.")
                    print(f"Total de gastos para el día {fecha_dia} en {base_moneda}: {total_diario}")
                            except ValueError:
                                print(f"El monto del gasto '{gasto.get('Monto del gasto')}' no es un número válido.")
                    print(f"Total de gastos para el día {fecha_dia}: {total_diario}")
                    return calcular()
        elif opcion=="2":
            fecha_inicio=input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin=input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            try:
                with open("informacion_De_Gastos.json","r") as Leer_json:
                    contenido=json.load(Leer_json)
                tasas = load_tasas()
                base_moneda = get_base_currency(tasas)
                total_semanal=0.0
                for gasto in contenido:
                    fecha_gasto=gasto.get("Fecha","")
                    if fecha_inicio <= fecha_gasto <= fecha_fin:
                        total_semanal += sumar_monto_base(gasto, tasas, base_moneda)
                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {base_moneda}: {total_semanal}")
            except FileNotFoundError:
                print("El archivo informacion_De_Gastos.json no existe.")
            except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
            return calcular()
        elif opcion=="3":         
            fecha_inicio=input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_fin=input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            try:
                with open("informacion_De_Gastos.json","r") as Leer_json:
                    contenido=json.load(Leer_json)
                tasas = load_tasas()
                base_moneda = get_base_currency(tasas)
                total_mensual=0.0
                for gasto in contenido:
                    fecha_gasto=gasto.get("Fecha","")
                    if fecha_inicio <= fecha_gasto <= fecha_fin:
                        total_mensual += sumar_monto_base(gasto, tasas, base_moneda)
                print(f"Total de gastos para el periodo {fecha_inicio} a {fecha_fin} en {base_moneda}: {total_mensual}")
            except FileNotFoundError:
                print("El archivo informacion_De_Gastos.json no existe.")
            except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
            return calcular()
        elif opcion=="4":
            return
        else:
            print("Opcion no valida, ingrese una opcion correcta")
            