import json
"""
aqui vamos a hacer las funciones donde es para guardar los diccionarios a las litas de json
para tener una permanencia tanto para os reportes como para los gastos
"""
def abrirJSON():
    dic=[]
    with open("./Data/data.json",'r') as openFile:
        dic=json.load(openFile)
    return dic

def guardarJSON(dic):
    with open("./Data/data.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs():
    dic=[]
    with open("./Data/dataReportes.json",'r') as openFile:
        dic=json.load(openFile)
    return dic

def logsJSON(dic):
    dicTemporal = []
    
    dicTemporal=cargarLogs()
    dicTemporal.append(dic)
    with open("./Data/dataReportes.json",'w') as outFile:
        json.dump(dicTemporal,outFile)



