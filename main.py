import json
from clase_Avion import Avion
from clase_persona import Pasajero
from clase_persona import Servicio
from clase_persona import Piloto
from clase_Sistema import Sistema
from clase_Vuelo import Vuelo

sistema = Sistema()

archivo = open("datos.json", "r")
diccionario = json.loads(archivo.read())
contador = 0

for i in diccionario["Aviones"]:
    avion = Avion()
    avion.AgregarAvion(i)
    sistema.AgregarAviones(avion)
    # print(avion)

for w in diccionario["Personas"]:

    if w["tipo"] == "Pasajero":
        pasajero = Pasajero()
        pasajero.AgregarPersona(w)
        pasajero.AgregarPasajero(w)
        sistema.AgregarPersonas(pasajero)
        # print (pasajero.nombre, pasajero.solicitudes_especiales)

    elif w["tipo"] == "Servicio":
        codigo = None
        objeto_avion = None
        lista_aviones = []
        servicio = Servicio()
        servicio.AgregarPersona(w)
        servicio.AgregarServicio(w)
        sistema.AgregarPersonas(servicio)
        # print (servicio.nombre, servicio.aviones_habilitados)

        for item in servicio.aviones_habilitados:
            codigo = item
            objeto_avion = sistema.BuscarAvion(codigo)
            lista_aviones.append(objeto_avion)
        servicio.aviones_habilitados = lista_aviones
        '''
        for item in servicio.aviones_habilitados:
            print(item, item.codigo)
        '''
    elif w["tipo"] == "Piloto":

        piloto = Piloto()
        lista_aviones = []
        codigo = None
        piloto.AgregarPersona(w)
        piloto.AgregarPiloto(w)
        sistema.AgregarPersonas(piloto)

        for item2 in piloto.aviones_habilitados_piloto:
            codigo = item2
            objeto_avion = sistema.BuscarAvion(codigo)
            lista_aviones.append(objeto_avion)

        piloto.aviones_habilitados_piloto = lista_aviones
        '''
        for item in piloto.aviones_habilitados_piloto:
            print(item, item.codigo)
        '''
for j in diccionario["Vuelos"]:
    vuelo = Vuelo()
    lista_pasajeros = []
    lista_tripulacion = []
    vuelo.AgregarVuelo(j)
    vuelo.Fecha = sistema.DeStringADate(vuelo.Fecha)
    codigo = vuelo.Avion
    vuelo.Avion = sistema.BuscarAvion(codigo)

    for item in vuelo.tripulacion:
        lista_tripulacion.append(sistema.BuscarPersona(item))

    vuelo.tripulacion = lista_tripulacion

    for item in vuelo.pasajeros:
        lista_pasajeros.append(sistema.BuscarPersona(item))

    vuelo.pasajeros = lista_pasajeros
    sistema.AgregarVuelos(vuelo)
'''
for item in sistema.vuelos:
   print(item.destino, item.Avion.codigo, item.Fecha)

   for item2 in item.tripulacion:
       print(item2.nombre)
   for item2 in item.pasajeros:
       print(item2.nombre)
   '''



# 1
'''
for item in sistema.vuelos:
   for item2 in item.pasajeros:
       print(item.destino,item2, item2.dni, item2.nombre, item2.apellido)
'''

#2
'''
for r in sistema.vuelos:
    for o in r.pasajeros:
        aux = pasajero.fecha_nac
        pasajero_menor=None
        for e in o.fecha_nac:
            if e<aux:
                pasajero_menor=e
                print (pasajero_menor.nombre)

'''


#6
'''
for t in sistema.vuelos:
    for y in t.pasajeros:
        if y.vip == 1:
           print (y.nombre, " Es VIP")
        if y.solicitudes_especiales != None:
            print("La solicitud especial de: ", y.nombre, " con DNI", y.dni, " es: ", y.solicitudes_especiales)
'''


#3
'''
list_vuelo = []
for e in sistema.vuelos:
    cantidad = len(e.tripulacion)
    trip_necesaria = int(e.Avion.cantidadTripulacionNecesaria)
    if trip_necesaria > cantidad:
        list_vuelo.append(e.destino)
print(list_vuelo)
'''


#7
'''
for u in sistema.vuelos:
    for t in u.tripulacion:
        if t.tipo == "Servicio":
            for j in t.idiomas:
                print(t.nombre, t.idiomas)
'''



