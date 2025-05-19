from datetime import *
from tabulate import *

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
            gastoDiario(totalGastos)
    else:
        print("No hay gastos registrados para el día de hoy. ")


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
    else:
        print("No hay gastos registrados para la semana. ")

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
        print(tabulate(gastoMensual, headers="keys", tablefmt="pipe"))
        print(f"\nTotal de gastos Mensual: {totalGastos}")
    else:
        print("No hay gastos registrados para el mes. ")
def gastoDiario(totalGastos):
    print(f"\nTotal Gastos: ${totalGastos}")

def totalesDiarios(listaGastos):
    fechaActual=datetime.today().date()
    gastosDiario=[]
    totalGastos=0
    for i in range (len(listaGastos)):
        fechaGasto=datetime.strptime(listaGastos[i]["fecha"], "%Y-%m-%d").date()
        if (fechaGasto == fechaActual):
            gastosDiario.append(listaGastos[i])
            listaTransporte=[]
            listaComida=[]
            campos=[]
            if(listaGastos[i]["categoria"] == "comida"):
                gasto = listaGastos[i]
                gasto_filtrado = {k: gasto[k] for k in campos}
                listaComida.append(gasto_filtrado)
                totalGastos +=listaGastos[i]["montoGasto"]
            if gastosDiario:
                print(f"-Comida: {totalGastos}")
            if (listaGastos[i]["categoria"] == "transporte"):
                gasto = listaGastos[i]
                totalGastos=0
                gasto_filtrado = {k: gasto[k] for k in campos}
                listaTransporte.append(gasto_filtrado)
                totalGastos +=listaGastos[i]["montoGasto"]
        if gastosDiario:
            print(f"-Transporte: {totalGastos}")

