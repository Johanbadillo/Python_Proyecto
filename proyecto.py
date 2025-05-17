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
from  tabulate  import  tabulate 
from time import time

listaGastos=abrirJSON()
booleano=True

while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    print("=============================================")
    print("         Simulador de Gasto Diario")
    print("=============================================")
#CRUD (CREATE , READ , UPDATE & DELETE)
    print("Seleccione una opción:")
    print(" ")
    print("1. Registrar nuevo gasto")
    print("2. Enumere los gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")
#Aqui le damos las opciones a los usuarios de las cuales pueden escoger para lo que necesitan 
    print(" ")
    print(" ")
    opcion=int(input("Porfa ingresa una opcion numerica: "))
    print(" ")
    print(" ")
    #Aqui es donde empezamos a saltar a las opciones que el usuario desea usar 
    #Opcion numero 1 es donde uno debe registrar los datos de los gastos nuevos
    if(opcion==1):
        print("=============================================")
        print("            Registrar Nuevo Gasto")
        print("=============================================")
        print("Ingrese la informacion del gasto:")
        print("  ")
        monto=int(input("- Monto del gasto:  "))
        unidades=str(input("- Cantidad: "))
        clase=str(input("- Categoria ( comida, transporte, entretenimientos, otros):  "))
        info=str(input("- Descripcion(opcional): "))
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":clase,
            "descripcion":info
        }
        confirmacion=input("Introduzca " ' s '"para guardar o " ' c ' "para cancelar: ")
        print("=============================================\n")
        
        if(confirmacion=='s'):
            listaGastos.append(dicGastonuevo)
            guardarJSON(listaGastos)
            print("Gasto nuevo guardado!!!")
        else:
            print("Gasto no ingresado")
        print(" ")

    if(opcion==2):
        print("=============================================")
        print("                Lista de gastos")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos:")
        print("")
        print("1. Ver todos los gastos")
        print("2. Filtrar por categoria")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")
        print("=============================================")
        confirmacion=int(input("Porfa ingrese una opcion numerica: "))
        
        if (confirmacion==1):
            print(listaGastos)
        elif (confirmacion==2):
            categoria=int(input("1. Comida, 2. Transporte, 3. Entretenimiento, 4. Otros"))
            if (categoria==1):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "comida"):
                        listaComida = [listaGastos[i]]
                        print(" ", listaComida)
                else:
                    print("No se encuentra gastos para la categoria de comida")
            elif(categoria==2):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "transporte"):
                        listaTransporte = [listaGastos[i]]
                        print(" ", listaTransporte)
                else:
                    print("No se encuentra gastos para la categoria de comida")
            elif(categoria==3):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "entretenimiento"):
                        listaEntretenimiento = [listaGastos[i]]
                        print(" ", listaEntretenimiento)
                else:
                    print("No se encuentra gastos para la categoria de entretenimiento")
            elif(categoria==4):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "otros"):
                        listaOtros = [listaGastos[i]]
                        print(" ", listaOtros)
                else:
                    print("No se encuentra gastos para la categoria de otros")
            else:
                print("No se encontro opcion valida \nRegresando al menu principal")
        elif(confirmacion==3):
            print("")
                
                        
                    


                    
                        

                













