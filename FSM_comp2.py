import json

with open('lib_comp2.json', 'r') as archivo:
    libreria_leida=json.load(archivo)
print(libreria_leida[0]['entrada'])

entrada=0
estado_actual=0
estado_siguiente=0
salida=0





