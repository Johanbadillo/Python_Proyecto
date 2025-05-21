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
from funcionesMensajes import *
from  tabulate  import  *
from datetime import *

listaGastos=abrirJSON()
booleano=True
cabeza=["monto","cantidad","categoria","descripcion","fecha"]
totalGastos=0
totales={}
temporal={}
while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    #CRUD (CREATE , READ , UPDATE & DELETE)
    mensajeIni()
    opcion=int(input(""))
    #Aqui es donde empezamos a saltar a las opciones que el usuario desea usar 
    #Opcion numero 1 es donde uno debe registrar los datos de los gastos nuevos
    if(opcion==1):
        mensaje1()
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
        mensaje2()
        confirmacion=int(input(""))
        filtroCate(confirmacion,listaGastos)
    if(opcion==3):
        mensaje3()
        calculoOpcion=int(input(""))
        calculos(calculoOpcion,listaGastos)
    if(opcion==4):
        mensaje4()
        opcion=int(input(""))
        if(opcion==1):
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - Diario: " + x)
            totalDiario(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesDiarios(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros)
                guardarlos(logsJSON, guardarJSON, temporal, listaGastos)
            else:
                print("")
        elif(opcion==2): 
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - semanal: " + x)
            totalSemanal(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesSemanales(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros)
            else:
                print("")
        elif(opcion==3):
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - mensual: " + x)
            totalMes(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesMensuales(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros)
            else:
                print("")
        elif(opcion==4):
            print("Regresando al menu principal")
        else:
            print("\nOpcion no valida\nRegresando al menu principal\n")
    elif(opcion==5):
            print("Gracias por usar el sistema de gestión de gastos. ¡Hasta la próxima!")
            booleano=False

