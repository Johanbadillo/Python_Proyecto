# ###################################
# ##########Python-Proyecto##########
# ################################### 
#
#Debemos crear un programa donde nos ayude a llevar nuestros gastos diarios 
#Donde se puedan monitorear,filtrar por categorias,calcular los totales por rango de periodo 
#Filtrandolo por periodos de tiempo
#Generar reportes y guardarlos en un archivo json

#En este lado importamos(osea traemos)los otros archivos que necesitamos 
#En este caso las funciones para el funcionamiento del programa 
#y las funciones para traer y llevar la base de los gastos
from Funciones.funciones import *
from Funciones.funcionesJson import *
from Funciones.funcionesMensajes import *
from  tabulate  import  *
from datetime import *
# traemos hasta aqui la base de datos tipo json que estaremos usando a lo largo del codigo
listaGastos=abrirJSON()
#aqui hacemos qu el ciclo while  se repita infinitamente hasta que no se cambie el valor a booleano
booleano=True
while(booleano):
    listaGastos=abrirJSON()
    #En este punto se actualiza la lista de gastos cada vez que se hace un cambio
    mensajeIni()
    #importamos el mensaje inicial 
    opcion=int(input(""))
    #Aqui es donde empezamos a saltar a las opciones que el usuario desea usar 
    #Opcion numero 1 es donde uno debe registrar los datos de los gastos nuevos
    if(opcion==1):
        mensaje1()
        #le pedimos los datos que desea agg el usuario 
        monto=int(input("- Monto del gasto:  "))
        unidades=int(input("- Cantidad: "))
        clase=str(input("Categorias:\n\nComida\nTransporte\nEntretenimiento\nSalud\nRopa\nTecnologia\nHogar\nOtros\n=============================================\n"))
        clase=clase.lower()
        info=str(input("- Descripcion(opcional): "))
        #aqui le preguntamos si quiere que la fecha se guarde de manea local con la hora de la pc o que el mismo usuario introduzca la hora qu deseas guardar el gastos
        opcionHoractual=int(input("1. ¿Quieres que guardes la Fecha actual? o 2. ¿Quieres guardar la fecha manualmente?"))
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
#Opcion numero2 aqui enumeramos gastos
    if(opcion==2):
        #y aqui traemos el mensaje que se encuentra en funciones mensajes
        mensaje2()
        confirmacion=int(input(""))
        filtroCate(confirmacion,listaGastos)
#Opcion numero3 aqui calculamos los totales de los gastos
    if(opcion==3):
        #y aqui traemos el mensaje que se encuentra en funciones mensajes
        mensaje3()
        calculoOpcion=int(input(""))
        calculos(calculoOpcion,listaGastos)
#Opcion numero4 aqui generamos los reportes
    if(opcion==4):
        #y aqui traemos el mensaje que se encuentra en funciones mensajes
        mensaje4()
        opcion=int(input(""))
        if(opcion==1):
            """
            aqui vamos a generar los reportes diarios primero dividiendo por rangos de tiempo los diarios solo van a tomar los valores del dia de hoy
            luego de filtra la lista por el rango del tiempo se va sacando los totales por cada categoria y se guarda en un archivo json
            """
            #aqui son los diarios
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - Diario: " + x)
            totalDiario(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesDiarios(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros,"Diario")
                guardarlos(logsJSON, guardarJSON, temporal, listaGastos)
            else:
                print("")
        #aqui son los semanales
        elif(opcion==2): 
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - semanal: " + x)
            totalSemanal(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesSemanales(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros,"Semanal")
                guardarlos(logsJSON, guardarJSON, temporal, listaGastos)
            else:
                print("")
        #aqui son los mensuales
        elif(opcion==3):
            x = str(date.today().strftime("%Y-%m-%d"))
            print("")
            print("Reporte Gastos - mensual: " + x)
            totalMes(listaGastos)
            print("\nCategorias:")
            (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros) = totalesMensuales(listaGastos)
            OpcionGuardado = int(input("¿Quieres guardar este registro?\n1. Si\n2. No\n"))
            if (OpcionGuardado == 1):
                temporal = guardarRepor(OpcionGuardado, totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros,"Mensual")
                guardarlos(logsJSON, guardarJSON, temporal, listaGastos)
            else:
                print("")
        #aqui se da la opcion de mostrar los reportes anteriores guardados
        elif(opcion==4):
            Reportes=cargarLogs()
            print(tabulate(Reportes, headers="keys", tablefmt="pipe"))
        elif(opcion==5):
            print("Regresando al menu principal")
        else:
            print("\nOpcion no valida\nRegresando al menu principal\n")
    elif(opcion==5):
            #aqui finalizamos las repeticiones de la lista de while 
            #haciendo que booleano sea falso y asi rompiendo las repeticiones
            print("Gracias por usar el sistema de gestión de gastos. ¡Hasta la próxima!")
            booleano=False

