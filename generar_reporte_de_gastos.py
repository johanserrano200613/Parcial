import json
def generar_reporte_de_gastos():
    print("""=============================================
           Generar Reporte de Gastos
=============================================
Seleccione el tipo de reporte:

1. Reporte diario
2. Reporte semanal
3. Reporte mensual
4. Regresar al menú principal
=============================================""")
    while True:
        opcion = input("Ingrese la opcion que desea realizar: ")

        if opcion == "1":
            fecha_dia = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
            try:
                with open("informacion_De_Gastos.json", "r") as Leer_json:
                    contenido = json.load(Leer_json)

                gastos_en_fecha = [
                    gasto for gasto in contenido
                    if str(gasto.get("Fecha", "")).strip() == fecha_dia
                ]

                print(f"Reporte de montos para el día {fecha_dia}:")

                if gastos_en_fecha:
                    total = 0.0
                    for gasto in gastos_en_fecha:
                        monto = gasto.get("Monto del gasto", gasto.get("Monto", "0"))
                        print(f"Monto: {monto}")
                        try:
                            total += float(monto)
                        except (ValueError, TypeError):
                            pass
    
                    print("""=============================================
1.Mostrar reporte en pantalla
2.Guardar reporte en .JSON
=============================================""")       
                    opcion4=input("Ingrese la opcion que desea realizar: ")
                    if opcion4=="1":
                        print(f"Total del día: {total}")
                        return generar_reporte_de_gastos()
                    elif opcion4=="2":
                        reporte = {
                            "Fecha": fecha_dia,
                            "Total": total,
                            "Gastos": gastos_en_fecha
                        }
                        with open("reporte_de_gastos.json", "w") as archivo_reporte:
                            json.dump(reporte, archivo_reporte, indent=4)
                        print("Reporte guardado en 'reporte_de_gastos.json'.")
                        return generar_reporte_de_gastos()
                else:
                    print(f"No se encontraron gastos en la fecha '{fecha_dia}'.")
            except FileNotFoundError:
                print("El archivo informacion_De_Gastos.json no existe.")
            except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
            except Exception as e:
                print(f"OCURRIO UN ERROR: {e}")

        elif opcion == "2":
            opcion = input("ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
            opcion2 = input("ingrese la fecha de fin (YYYY-MM-DD): ").strip() 
            try:
                with open("informacion_De_Gastos.json", "r") as Leer_json:
                    contenido = json.load(Leer_json)

                gastos_en_periodo = [
                    gasto for gasto in contenido
                    if opcion <= str(gasto.get("Fecha", "")).strip() <= opcion2
                ]

                print(f"Reporte de montos para el periodo {opcion} a {opcion2}:")

                if gastos_en_periodo:
                    total = 0.0
                    for gasto in gastos_en_periodo:
                        monto = gasto.get("Monto del gasto", gasto.get("Monto", "0"))
                        print(f"Monto: {monto}")
                        try:
                            total += float(monto)
                        except (ValueError, TypeError):
                            pass
                    print("""=============================================
1.Mostrar reporte en pantalla
2.Guardar reporte en .JSON
=============================================""")       
                    opcion3=input("Ingrese la opcion que desea realizar: ")
                    if opcion3=="1":
                        print(f"Total del periodo: {total}")
                        return generar_reporte_de_gastos()
                    elif opcion3=="2":
                        reporte = {
                            "Periodo": f"{opcion} a {opcion2}",
                            "Total": total,
                            "Gastos": gastos_en_periodo
                        }
                        with open("reporte_de_gastos.json", "w") as archivo_reporte:
                            json.dump(reporte, archivo_reporte, indent=4)
                        print("Reporte guardado en 'reporte_de_gastos.json'.")
                        return generar_reporte_de_gastos()
                else:
                    print(f"No se encontraron gastos entre las fechas '{opcion}' y '{opcion2}'.")
            except FileNotFoundError:
                print("El archivo informacion_De_Gastos.json no existe.")
            except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
            except Exception as e:
                print(f"OCURRIO UN ERROR: {e}")
        elif opcion == "3":
            opcion = input("ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
            opcion2 = input("ingrese la fecha de fin (YYYY-MM-DD): ").strip()
            try:
                with open("informacion_De_Gastos.json", "r") as Leer_json:
                    contenido = json.load(Leer_json)

                gastos_en_periodo = [
                    gasto for gasto in contenido
                    if opcion <= str(gasto.get("Fecha", "")).strip() <= opcion2
                ]

                print(f"Reporte de montos para el periodo {opcion} a {opcion2}:")

                if gastos_en_periodo:
                    total = 0.0
                    for gasto in gastos_en_periodo:
                        monto = gasto.get("Monto del gasto", gasto.get("Monto", "0"))
                        print(f"Monto: {monto}")
                        try:
                            total += float(monto)
                        except (ValueError, TypeError):
                            pass
                    print("""=============================================
1.Mostrar reporte en pantalla
2.Guardar reporte en .JSON
=============================================""")   
                    opcion2=input("Ingrese la opcion que desea realizar: ")
                    if opcion2=="1":
                        print(f"Total del periodo: {total}")
                        return generar_reporte_de_gastos()
                    elif opcion2=="2":
                        reporte = {
                            "Periodo": f"{opcion} a {opcion2}",
                            "Total": total,
                            "Gastos": gastos_en_periodo
                        }
                        with open("reporte_de_gastos.json", "w") as archivo_reporte:
                            json.dump(reporte, archivo_reporte, indent=4)
                        print("Reporte guardado en 'reporte_de_gastos.json'.")
                        return generar_reporte_de_gastos()
                else:
                    print(f"No se encontraron gastos entre las fechas '{opcion}' y '{opcion2}'.")
            except FileNotFoundError:
                print("El archivo informacion_De_Gastos.json no existe.")
            except json.JSONDecodeError:
                print("El archivo informacion_De_Gastos.json contiene JSON inválido.")
            except Exception as e:
                print(f"OCURRIO UN ERROR: {e}")
        elif opcion == "4":
            return
        else:
            print("Opción no válida, ingrese una opción correcta")

    