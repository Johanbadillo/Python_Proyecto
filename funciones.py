from datetime import *
from tabulate import *


def filtroCate(confirmacion,listaGastos):
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


def calculos(calculoOpcion,listaGastos):
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
            print(f"\nTotal Gastos: ${totalGastos}")
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
        print(f"\nTotal de gastos de la semana: {totalGastos}")
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
        print(f"\nTotal de gastos Mensual: {totalGastos}")


def totalesDiarios(listaGastos):
    fechaActual=datetime.today().date()
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaGasto == fechaActual):
            gastosReportes.append(listaGastos[i])
    reportes(gastosReportes)
def totalesSemanales(listaGastos):
    fechaActual=datetime.today().date()
    fechaSemanal=fechaActual-timedelta(days=7)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaSemanal <= fechaGasto <= fechaActual):
            gastosReportes.append(listaGastos[i])
    reportes(gastosReportes)
def totalesMensuales(listaGastos):
    fechaActual=datetime.today().date()
    fechaMensual=fechaActual-timedelta(days=30)
    gastosReportes=[]
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaMensual <= fechaGasto <= fechaActual):
            gastosReportes.append(listaGastos[i])
    reportes(gastosReportes)


def reportes(gastosReportes):
        totalGastosComida = 0
        totalGastosTransporte = 0
        totalGastosEntretenimiento = 0
        totalGastosSalud = 0
        totalGastosRopa = 0
        totalGastosTecnologia = 0
        totalGastosHogar = 0
        totalGastosOtros = 0
        for i in gastosReportes:
            if(i["categoria"] == "comida"):
                totalGastosComida +=i["montoGasto"]
            if (i["categoria"] == "transporte"):
                totalGastosTransporte +=i["montoGasto"]
            if (i["categoria"] == "entretenimiento"):
                totalGastosEntretenimiento +=i["montoGasto"]
            if (i["categoria"] == "salud"):
                totalGastosSalud +=i["montoGasto"]
            if (i["categoria"] == "ropa"):
                totalGastosRopa +=i["montoGasto"]
            if (i["categoria"] == "tecnologia"):
                totalGastosTecnologia +=i["montoGasto"]
            if (i["categoria"] == "hogar"):
                totalGastosHogar +=i["montoGasto"]
            if (i["categoria"] == "otros"):
                totalGastosOtros +=i["montoGasto"]
        print(f"-Comida: ${totalGastosComida}\
            \n-Transporte: ${totalGastosTransporte}\
            \n-Entretenimiento: ${totalGastosEntretenimiento}\
            \n-Salud: ${totalGastosSalud}\
            \n-Ropa: ${totalGastosRopa}\
            \n-Tecnologia: ${totalGastosTecnologia}\
            \n-Hogar: ${totalGastosHogar}\
            \n-Otros: ${totalGastosOtros}")