import json
from clase_Avion import Avion
from clase_persona import Pasajero
from clase_persona import Servicio
from clase_persona import Piloto
from clase_Sistema import Sistema
from clase_Vuelo import Vuelo


sistema=Sistema()

archivo=open("datos.json", "r")
diccionario= json.loads(archivo.read())
contador = 0

for i in diccionario["Aviones"]:
    avion=Avion()
    avion.AgregarAvion(i)
    sistema.AgregarAviones(avion)
    #print(avion)


for w in diccionario["Personas"]:

    if w["tipo"] == "Pasajero":
        pasajero = Pasajero()
        pasajero.AgregarPersona(w)
        pasajero.AgregarPasajero(w)
        sistema.AgregarPersonas(pasajero)
        #print (pasajero.nombre, pasajero.solicitudes_especiales)

    elif w["tipo"] == "Servicio":
        codigo=None
        objeto_avion = None
        lista_aviones = []
        servicio = Servicio()
        servicio.AgregarPersona(w)
        servicio.AgregarServicio(w)
        sistema.AgregarPersonas(servicio)
        #print (servicio.nombre, servicio.aviones_habilitados)

        for item in sistema.aviones:
            codigo=item.codigo
            objeto_avion = sistema.BuscarAvion(codigo)
            lista_aviones.append(objeto_avion)
        servicio.aviones_habilitados = lista_aviones
        for item in servicio.aviones_habilitados:
            print(item, item.codigo)
    elif w["tipo"] == "Piloto":
        piloto = Piloto()
        piloto.AgregarPersona(w)
        piloto.AgregarPiloto(w)
        sistema.AgregarPersonas(piloto)
        #print(piloto.nombre, piloto.aviones_habilitados_piloto)


for j in diccionario["Vuelos"]:
    vuelo=Vuelo()
    vuelo.AgregarVuelo(j)
    sistema.AgregarVuelos(vuelo)
'''
for item in sistema.vuelos:
    print(item.destino, item.Avion, item.tripulacion, item.pasajeros)
'''


