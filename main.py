import json
from clase_Avion import Avion
from clase_persona import Pasajero
from clase_persona import Servicio
from clase_persona import Piloto

avion=Avion()
pasajero=Pasajero()
servicio=Servicio()
piloto=Piloto()




archivo=open("datos.json", "r")
diccionario= json.loads(archivo.read())


'''
for w in diccionario["Personas"]:
    if w["tipo"] == "Pasajero":
        pasajero.AgregarPersona(w)
        pasajero.AgregarPasajero(w)
        print (pasajero.nombre)

'''

for w in diccionario["Personas"]:
    if w["tipo"] == "Servicio":
        servicio.AgregarPersona(w)
        servicio.AgregarServicio(w)
        print (servicio.nombre)




'''
 for i in diccionario["Aviones"]:
   avion.AgregarAvion(i)
   print (avion.codigo)                     
'''


