import json

def abrirJSON():
    dic=[]
    with open("./data.json",'r') as openFile:
        dic=json.load(openFile)
    return dic

def guardarJSON(dic):
    with open("./data.json",'w') as outFile:
        json.dump(dic,outFile)

def cargarLogs():
    dic=[]
    with open("./dataReportes.json",'r') as openFile:
        dic=json.load(openFile)
    return dic

def logsJSON(dic):
    dicTemporal = []
    
    dicTemporal=cargarLogs()
    dicTemporal.append(dic)
    with open("./dataReportes.json",'w') as outFile:
        json.dump(dicTemporal,outFile)