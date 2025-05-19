# ###################################
# ##########Python-Proyecto##########
# ###################################

#Debemos crear un programa donde nos ayude a llevar nuestros gastos diarios 
#Donde se puedan monitorear,modificar,mostrary eliminar
#Filtrandolo por periodos de tiempo


#En este lado importamos(osea traemos)los otros archivos que necesitamos 
#En este caso las funciones para el funcionamiento del programa 
#y las funciones para traer y llevar la base de los gastos
from funciones import *
from funcionesJson import *
from  tabulate  import  *
from datetime import *

listaGastos=abrirJSON()
booleano=True
cabeza=["monto","cantidad","categoria","descripcion","fecha"]
totalGastos=0

while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("=============================================\
    \n         Simulador de Gasto Diario\
    \n=============================================\
    \nSeleccione una opción:\
    \n\
    \n1. Registrar nuevo gasto\
    \n2. Enumere los gastos\
    \n3. Calcular total de gastos\
    \n4. Generar reporte de gastos\
    \n5. Salir\
    \n=============================================")
    opcion=int(input(""))
    #Aqui es donde empezamos a saltar a las opciones que el usuario desea usar 
    #Opcion numero 1 es donde uno debe registrar los datos de los gastos nuevos
    if(opcion==1):
        print("=============================================\
            \n            Registrar Nuevo Gasto\
        \n=============================================\
        \nIngrese la informacion del gasto:\
        \n")
        monto=int(input("- Monto del gasto:  "))
        unidades=str(input("- Cantidad: "))
        clase=str(input("- Categoria ( comida, transporte, entretenimientos, otros):  "))
        info=str(input("- Descripcion(opcional): "))
        opcionHoractual=int(input("1. ¿Quieres que guardes la hora actual? o 2. ¿Quieres guardar la fecha manualmente?"))
        if(opcionHoractual==1):
            x= str(date.today().strftime("%Y-%m-%d"))
            print("Fecha guardada con exito")
            dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":clase,
            "descripcion":info,
            "fecha":x
        }
        if(opcionHoractual==2):
            fechaIngreso=input("Ingrese la fecha actual (formato YYYY-MM-DD): ")
            fecha = datetime.strptime(fechaIngreso, "%Y-%m-%d")
            print("Fecha guardada con exito")
            dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":clase,
            "descripcion":info,
            "fecha":fechaIngreso
        }
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        confirmacion=input("Introduzca " ' s '"para guardar o " ' c ' "para cancelar: ")
        print("=============================================")
        if((confirmacion=='s') or (confirmacion=='S')):
            listaGastos.append(dicGastonuevo)
            guardarJSON(listaGastos)
            print("Gasto nuevo guardado")
        else:
            print("Gasto no ingresado")
    if(opcion==2):
        print("=============================================\
            \n                Listar Gastos\
            \n=============================================\
            \nSeleccione una opción para filtrar los gastos:\
            \n""\
            \n1. Ver todos los gastos\
            \n2. Filtrar por categoria\
            \n3. Filtrar por rango de fechas\
            \n4. Regresar al menú principal\
            \n=============================================")
        confirmacion=int(input(""))
        print("=============================================")
        
        if (confirmacion==1):
            print(tabulate(listaGastos, tablefmt="double_outline"))
        elif (confirmacion==2):
            categoria=int(input("1. Comida\n2. Transporte\n3. Entretenimiento\n4. Salud\n5. Ropa\n6. Tecnologia\n7. Hogar\n8. Otros\n=============================================\n"))
            if categoria == 1:
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaComida = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "comida":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaComida.append(gasto_filtrado)
                if listaComida:
                    print(tabulate(listaComida, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de comida")
            elif(categoria==2):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaTransporte = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "transporte":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaTransporte.append(gasto_filtrado)
                if listaTransporte:
                    print(tabulate(listaTransporte, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de transporte")
            elif(categoria==3):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaEntretenimiento = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "entretenimiento":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaEntretenimiento.append(gasto_filtrado)
                if listaEntretenimiento:
                    print(tabulate(listaEntretenimiento, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de entretenimiento")
            elif(categoria==4):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaSalud = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "salud":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaSalud.append(gasto_filtrado)
                if listaSalud:
                    print(tabulate(listaSalud, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de salud")
            elif(categoria==5):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaRopa = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "ropa":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaRopa.append(gasto_filtrado)
                if listaRopa:
                    print(tabulate(listaRopa, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de ropa")
            elif(categoria==6):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaTecnología = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "tecnología":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaTecnología.append(gasto_filtrado)
                if listaTecnología:
                    print(tabulate(listaTecnología, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de tecnología")
            elif(categoria==7):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaHogar = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "hogar":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaHogar.append(gasto_filtrado)
                if listaHogar:
                    print(tabulate(listaHogar, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de hogar")
            elif(categoria==8):
                campos = ["fecha", "montoGasto", "categoria","cantidad"]
                listaOtros = []
                for i in range(len(listaGastos)):
                    if listaGastos[i]["categoria"] == "otros":
                        gasto = listaGastos[i]
                        gasto_filtrado = {k: gasto[k] for k in campos}
                        listaOtros.append(gasto_filtrado)
                if listaOtros:
                    print(tabulate(listaOtros, headers="keys", tablefmt="pipe"))
                else:
                    print("No hay gastos registrados para la clase de comida")
            else:
                print("=============================================\nNo se encontro opcion valida \nRegresando al menu principal")
        elif(confirmacion==3):
            campos=["fecha", "montoGasto", "categoria","descripcion","cantidad"]
            listaFecharango=[]
            fechaInicio=input("Ingrese la fecha inicial de la busqueda(formato YYYY-MM-DD): ")
            fechaInicio = datetime.strptime(fechaInicio, "%Y-%m-%d").date()      
            fechaFinal=input("Ingrese la fecha final de la busqueda (formato YYYY-MM-DD): ")
            fechaFinal = datetime.strptime(fechaFinal, "%Y-%m-%d").date()
            for gasto in listaGastos:
                fecha_gasto = datetime.strptime(gasto["fecha"], "%Y-%m-%d").date()
                if fechaInicio <= fecha_gasto <= fechaFinal:
                    gasto_filtrado = {k: gasto[k] for k in campos}
                    listaFecharango.append(gasto_filtrado)
            if listaFecharango:
                print(tabulate(listaFecharango, headers="keys", tablefmt="pipe"))
            else:
                print("No hay gastos que cumplan con la condición.")
        elif(confirmacion==4):
            print("Regresando al menú principal.........")
        else:
            print("\nOpcion no valida\nRegresando al menu principal.......\n")
    if(opcion==3):
        print("=============================================\
            \n          Calcular Total de Gastos\
            \n=============================================\
            \nSeleccione el periodo de cálculo:\
            \n\
            \n1. Calcular total diario\
            \n2. Calcular total semanal\
            \n3. Calcular total mensual\
            \n4. Regresar al menú principal\
            \n============================================= ")
        calculoOpcion=int(input(""))
        if(calculoOpcion == 1 ):
            totalDiario(listaGastos)
        elif(calculoOpcion==2):
            totalSemanal(listaGastos)
        elif(calculoOpcion==3):
            totalMes(listaGastos)
        elif(calculoOpcion==4):
            print("Regresando al menu principal")
        else:
            print("\nOpcion no valida\nRegresando al menu principal\n")
    if(opcion==4):
        print("=============================================\
            \n           Generar Reporte de Gastos\
            \n=============================================\
            \nSeleccione el tipo de reporte:\
            \n\
            \n1. Reporte diario\
            \n2. Reporte semanal\
            \n3. Reporte mensual\
            \n4. Regresar al menú principal\
            \n=============================================")
        opcion=int(input(""))
        if(opcion==1):
            x= str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - Dia: "+x)
            totalDiario(listaGastos)
            print("\n\nCategorias:")
            totalesDiarios(listaGastos,json)
        elif(opcion==2): 
            print("")
        elif(opcion==3):
            print("")
        elif(opcion==4):
            print("")
        else:
            print("\nOpcion no valida\nRegresando al menu principal\n")
    elif(opcion==5):
        print("Gracias por usar el sistema de gestión de gastos. ¡Hasta la próxima!")
        booleano=False
    














