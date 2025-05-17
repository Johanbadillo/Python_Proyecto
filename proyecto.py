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
        #Aqui hacemos un for para confirmar si deseas guardar el gasto
        print(" ")
        dicGastonuevo={
            "montoGasto":monto,
            "cantidad":unidades,
            "categoria":clase,
            "descripcion":info
        }
        confirmacion=input("Introduzca " ' s '"para guardar o " ' c ' "para cancelar: ")
        print("=============================================")
        
        if(confirmacion=='s'):
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
            print(listaGastos)
        elif (confirmacion==2):
            categoria=int(input("1. Comida\n2. Transporte\n3. Entretenimiento\n4. Otros"))
            if (categoria==1):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "comida"):
                        listaComida = [listaGastos[i]]
                        print(" ", listaComida)
                else:
                    print("\nNo se encuentra gastos para la categoria de comida")
            elif(categoria==2):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "transporte"):
                        listaTransporte = [listaGastos[i]]
                        print(" ", listaTransporte)
                else:
                    print("\nNo se encuentra gastos para la categoria de transporte")
            elif(categoria==3):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "entretenimiento"):
                        listaEntretenimiento = [listaGastos[i]]
                        print(" ", listaEntretenimiento)
                else:
                    print("\nNo se encuentra gastos para la categoria de entretenimiento")
            elif(categoria==4):
                for i in range(len(listaGastos)):
                    if( listaGastos[i]["categoria"] == "otros"):
                        listaOtros = [listaGastos[i]]
                        print(" ", listaOtros)
                else:
                    print("\nNo se encuentra gastos para la categoria de otros")
            else:
                print("=============================================\nNo se encontro opcion valida \nRegresando al menu principal")
        elif(confirmacion==3):
            fechaInicio=int(input("Ingrese la fecha del inicio de busqueda"))
            fechaFinal=(int(input("Ingrese la fecha del final de busqueda")))
        elif(confirmacion==4):
            print("Regresando al menú principal")
        else:
            print("\nOpcion no valida\nRegresando al menu principal\n")
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
        opcionCalculo=int(input(""))
        if(opcionCalculo==1):
           print("")


            
        




                
                        
                    


                    
                        

                













