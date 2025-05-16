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
    with open("./data/logs.json",'r') as openFile:
        dic=json.load(openFile)
    return dic