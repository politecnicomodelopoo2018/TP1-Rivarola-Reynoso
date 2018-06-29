from clase_Avion import Avion
from datetime import datetime
class Sistema (object):
   def __init__(self):
       self.personas=[]
       self.aviones=[]
       self.vuelos=[]

   def AgregarAviones(self,Avion):
       self.aviones.append(Avion)

   def AgregarPersonas(self,Persona):
       self.personas.append(Persona)

   def AgregarVuelos(self,Vuelo):
       self.vuelos.append(Vuelo)

   def BuscarAvion(self,codigo_avion):
       for item in self.aviones:
           if codigo_avion== item.codigo:
               return item


   def BuscarPersona(self,dni):
       for item in self.personas:
           if dni== item.dni:
               return item

   def DeStringADate(self, fecha):
       fecha_date = datetime.strptime(fecha, '%Y-%m-%d')
       return fecha_date
