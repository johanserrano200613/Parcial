import json
from datetime import date
import os
from moneda_utils import load_tasas, get_base_currency, normalize_currency

def Registrar_nuevo_gasto():
    while True :
        print("""=============================================
            Registrar Nuevo Gasto
=============================================
Ingrese la información del gasto:

- Monto del gasto:
- Categoría (ej. comida, transporte, entretenimiento, otros):
- Descripción (opcional):""")
        opcion = (input("\nIngrese 'S' para guardar o 'C' para cancelar:"))
        print("=============================================")
        if opcion.lower() == "s":
            try:
                try:            
                    Monto_del_gasto=float(input("-Monto del gasto:" ))
                except ValueError:
                    print("Error: Por favor, ingrese un número válido para el monto del gasto.")
                    return Registrar_nuevo_gasto()
                print("""=============================================
Categorias disponibles:
=============================================                                       
-comida
-transporte
-entretenimiento
-otros
=============================================""")
                Categoria=(input("-Categoría: ")).lower()
                if Categoria not in ["comida", "transporte", "entretenimiento", "otros"]:
                    print("Error: Por favor, ingrese una categoría válida.")
                    return Registrar_nuevo_gasto()
            except:
                print("Ocurrio un error, ingrese los datos correctamente")
                return Registrar_nuevo_gasto()

            tasas = load_tasas()
            moneda_por_defecto = get_base_currency(tasas)
            moneda_gasto = input(f"-Moneda (ej. COP, USD, EUR) [default {moneda_por_defecto}]: ").strip().upper()
            if not moneda_gasto:
                moneda_gasto = moneda_por_defecto or "COP"

            de_descripcion=input("Quieres añadirle descripcion? (s/n): ")
            if de_descripcion.lower()=="s":
                Descripcion=input("-Descripcion: ")
            else:
                Descripcion="N/A"
            Fecha=date.today().strftime("%Y-%m-%d")
            objeto_json={
                "Monto del gasto":Monto_del_gasto,
                "Moneda":normalize_currency(moneda_gasto),
                "Categoria":Categoria,
                "Descripcion":Descripcion,
                "Fecha":Fecha
            }
            Informacion_De_Gastos=[]
            if os.path.exists("informacion_De_Gastos.json"):
                with open("informacion_De_Gastos.json","r")as Leer_json:
                    contenido=Leer_json.read()
                    if contenido:
                        try:
                            Informacion_De_Gastos=json.loads(contenido)

                        except json.JSONDecodeError as e:
                            print(f"OCURRIO UN ERROR: {e}")
                            Informacion_De_Gastos=[]

            Informacion_De_Gastos.append(objeto_json)

            with open("informacion_De_Gastos.json","w") as escribir:
                json.dump(Informacion_De_Gastos,escribir)
                print("Gasto registrado correctamente")
                break
            


        elif opcion.lower()== "c":
            return
        else:
            print("Opciòn no valida")

