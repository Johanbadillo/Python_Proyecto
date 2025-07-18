"""
aqui vamos a declarar las funciones que vamos a usar a lo largo del archivo proyecto hacindo que haga procesos repetitivos 
importando tambien las libreria de tiempo y tabular 
"""

from datetime import *
from tabulate import *

#En esta opcion vamos a estar filtrando los totales por categoria una por una comparandolas
def filtroCate(confirmacion,listaGastos):
    print("=============================================")
    if (confirmacion==1):
        print(tabulate(listaGastos, tablefmt="double_outline"))
    elif (confirmacion==2):
        categoria=int(input("1. Comida\n2. Transporte\n3. Entretenimiento\n4. Salud\n5. Ropa\n6. Tecnologia\n7. Hogar\n8. Otros\n=============================================\n"))
        if categoria == 1:
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            campos = ["fecha", "montoGasto", "categoria","cantidad","descripcion"]
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
            print(tabulate(listaFecharango, tablefmt="heavy_outline"))
        else:
            print("No hay gastos que cumplan con la condición.")
    elif(confirmacion==4):
        print("Regresando al menú principal.........")
    else:
        print("\nOpcion no valida\nRegresando al menu principal.......\n")

#aqui definimos la funcion de calculo que en cada opcion esta definida en otro lugar
def calculos(calculoOpcion,listaGastos):
    if(calculoOpcion == 1 ):
        totalDiario(listaGastos)
        print("")
        totalesDiarios(listaGastos)
    elif(calculoOpcion==2):
        totalSemanal(listaGastos)
        print("")
        totalesSemanales(listaGastos)
    elif(calculoOpcion==3):
        totalMes(listaGastos)
        print("")
        totalesMensuales(listaGastos)
    elif(calculoOpcion==4):
        print("Regresando al menu principal")
    else:
        print("\nOpcion no valida\nRegresando al menu principal\n")
#aqui esta la funcion de los totales dependiendo por el rango de tiempo
#en esta primera opcion es diaria
def totalDiario(listaGastos):
    fechaActual=datetime.today().date()
    gastosDiario=[]
    totalGastos=0
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaGasto == fechaActual):
            gastosDiario.append(listaGastos[i])
            totalGastos +=listaGastos[i]["montoGasto"]
    if gastosDiario:
        print(f"\nTotal de los gastos Diarios: ${totalGastos}")
    else:
        print(f"\nTotal de los gastos Diarios: ${totalGastos}")
#aqui es por semanas
def totalSemanal(listaGastos):
    fechaActual=datetime.today().date()
    fechaSemanal=fechaActual-timedelta(days=7)
    gastoSemanal=[]
    totalGastos=0
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaSemanal <= fechaGasto <= fechaActual):
            gastoSemanal.append(listaGastos[i])
            totalGastos +=listaGastos[i]["montoGasto"]
    if gastoSemanal:
        print(f"\nTotal de los gastos Semanales: ${totalGastos}")
    else:
        print(f"\nTotal de los gastos Semanales: ${totalGastos}")
        #aqui es por meses
def totalMes(listaGastos):
    fechaActual=datetime.today().date()
    fechaMensual=fechaActual-timedelta(days=30)
    gastoMensual=[]
    totalGastos=0
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaMensual <= fechaGasto <= fechaActual):
            gastoMensual.append(listaGastos[i])
            totalGastos +=listaGastos[i]["montoGasto"]
    if gastoMensual:
        print(f"\nTotal de los gastos Mensuales: ${totalGastos}")
    else:
        print(f"\nTotal de los gastos Mensuales: ${totalGastos}")
"""
Aqui lo que vamos a definir son los totales de cada categoria pero los datos ingresados seran filtrados por la funciones que vienen
que puede ser diaria,semanales o mensuales 
donde saca el total para cada categoria y regresando el valor para cada una
"""
#aqui es cuando son diarios
def totalesDiarios(listaGastos):
    fechaActual=datetime.today().date()
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaGasto == fechaActual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)
#aqui son las semanales
def totalesSemanales(listaGastos):
    fechaActual=datetime.today().date()
    fechaSemanal=fechaActual-timedelta(days=7)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaSemanal <= fechaGasto <= fechaActual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)
#aqui son las mensuals
def totalesMensuales(listaGastos):
    fechaActual=datetime.today().date()
    fechaMensual=fechaActual-timedelta(days=30)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaMensual <= fechaGasto <= fechaActual):
            gastosReportes.append(listaGastos[i])
    return reportes(gastosReportes)

"""
Aqui vamos a sacar los totales difiniendo las variables y haiendo regresar los valores para cada categoria
y haciendolas añadir a una lista 
"""
def reportes(gastosReportes):
    totalGastosComida = 0
    totalGastosTransporte = 0
    totalGastosEntretenimiento = 0
    totalGastosSalud = 0
    totalGastosRopa = 0
    totalGastosTecnologia = 0
    totalGastosHogar = 0
    totalGastosOtros = 0
    totales = {
        "comida": 0,
        "transporte": 0,
        "entretenimiento": 0,
        "salud": 0,
        "ropa": 0,
        "tecnologia": 0,
        "hogar": 0,
        "otros": 0
    }
    for i in gastosReportes:
        totalGastosComida = comida(i, totales, totalGastosComida)
        totalGastosTransporte = transporte(i, totales, totalGastosTransporte)
        totalGastosEntretenimiento = entretenimiento(i, totales, totalGastosEntretenimiento)
        totalGastosSalud = salud(i, totales, totalGastosSalud)
        totalGastosRopa = ropa(i, totales, totalGastosRopa)
        totalGastosTecnologia = tecnologia(i, totales, totalGastosTecnologia)
        totalGastosHogar = hogar(i, totales, totalGastosHogar)
        totalGastosOtros = otros(i, totales, totalGastosOtros)
    print(f"-Comida: ${totalGastosComida}\
        \n-Transporte: ${totalGastosTransporte}\
        \n-Entretenimiento: ${totalGastosEntretenimiento}\
        \n-Salud: ${totalGastosSalud}\
        \n-Ropa: ${totalGastosRopa}\
        \n-Tecnologia: ${totalGastosTecnologia}\
        \n-Hogar: ${totalGastosHogar}\
        \n-Otros: ${totalGastosOtros}")
    return (totalGastosComida, totales, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros)
#aqui hacemos funciones donde muestra el total de cada categoria
def comida(i, totales, totalGastosComida):
    if i["categoria"] == "comida":
        totalGastosComida += i["montoGasto"]
        totales["comida"] = totalGastosComida
    return totalGastosComida
def transporte(i, totales, totalGastosTransporte):
    if i["categoria"] == "transporte":
        totalGastosTransporte += i["montoGasto"]
        totales["transporte"] = totalGastosTransporte
    return totalGastosTransporte
def entretenimiento(i, totales, totalGastosEntretenimiento):
    if i["categoria"] == "entretenimiento":
        totalGastosEntretenimiento += i["montoGasto"]
        totales["entretenimiento"] = totalGastosEntretenimiento
    return totalGastosEntretenimiento
def salud(i, totales, totalGastosSalud):
    if i["categoria"] == "salud":
        totalGastosSalud += i["montoGasto"]
        totales["salud"] = totalGastosSalud
    return totalGastosSalud
def ropa(i, totales, totalGastosRopa):
    if i["categoria"] == "ropa":
        totalGastosRopa += i["montoGasto"]
        totales["ropa"] = totalGastosRopa
    return totalGastosRopa
def tecnologia(i, totales, totalGastosTecnologia):
    if i["categoria"] == "tecnologia":
        totalGastosTecnologia += i["montoGasto"]
        totales["tecnologia"] = totalGastosTecnologia
    return totalGastosTecnologia
def hogar(i, totales, totalGastosHogar):
    if i["categoria"] == "hogar":
        totalGastosHogar += i["montoGasto"]
        totales["hogar"] = totalGastosHogar
    return totalGastosHogar
def otros(i, totales, totalGastosOtros):
    if i["categoria"] == "otros":
        totalGastosOtros += i["montoGasto"]
        totales["otros"] = totalGastosOtros
    return totalGastosOtros

#aqui guardamos los totales a cada tipo de categoria y regresando la lista
def guardarRepor(OpcionGuardado,totalGastosComida, totalGastosTransporte, totalGastosEntretenimiento, totalGastosSalud, totalGastosRopa, totalGastosTecnologia, totalGastosHogar, totalGastosOtros,tipo_reporte):
    temporal={}
    if OpcionGuardado == 1:
        temporal = {
            "tipo_reporte":tipo_reporte,
            "comida": totalGastosComida,  
            "transporte": totalGastosTransporte, 
            "entretenimiento": totalGastosEntretenimiento,  
            "salud": totalGastosSalud,  
            "ropa": totalGastosRopa,  
            "tecnologia": totalGastosTecnologia, 
            "hogar": totalGastosHogar,  
            "otros": totalGastosOtros
        }
    else:
        print("") 
    return temporal
#aqui guardamos la lista
def guardarlos(logsJSON, guardarJSON, temporal, listaGastos):
        logsJSON(temporal)
        guardarJSON(listaGastos)
