from Registrar_nuevo_gasto import Registrar_nuevo_gasto
from Lista_de_gastos import lista_de_gastos
from calcular_total_de_gastos import calcular
from generar_reporte_de_gastos import generar_reporte_de_gastos     
from recalcular_moneda import recalcular_multimoneda

def main():
    while True :
        print("""=============================================
         Simulador de Gasto Diario
=============================================
Seleccione una opción:

1. Registrar nuevo gasto
2. Listar gastos
3. Calcular total de gastos
4. Generar reporte de gastos
5. Calcular cambio de moneda
6. Salir
=============================================""")
        opcion = (input("Ingrese lo que quiere realizar: "))
        if opcion == "1":
             Registrar_nuevo_gasto()
        elif  opcion == "2":
            lista_de_gastos()
        elif opcion == "3":
            calcular()
        elif opcion == "4":
            generar_reporte_de_gastos()
        elif  opcion == "5":
            recalcular_multimoneda()
        elif  opcion == "6":
            print("Saliendo..............")
            break
        else:
            print("Opciòn no valida")



while True :
        ingresa = input("¿Desea realizar una compra? (s/n): ")
        if ingresa.lower() == 's':
            main()
        if ingresa.lower() == 'n':
            print("SALIENDO...")
            break
        if ingresa.lower()!="s"  or "n":
            print("Ocurrio un error ingrese caracter correcto")


