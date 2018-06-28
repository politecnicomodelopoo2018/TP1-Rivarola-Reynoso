class Vuelo(object):
    Avion=None
    Fecha=None
    hora=None
    origen=None
    destino=None

    def __init__(self):
        self.tripulacion=[]
        self.pasajeros=[]

    def AgregarVuelo(self,Vuelo):
        self.Avion=Vuelo["avion"]
        self.Fecha=Vuelo["fecha"]
        self.hora=Vuelo["hora"]
        self.origen=Vuelo["origen"]
        self.destino=Vuelo["destino"]
        self.tripulacion=Vuelo["tripulacion"]
        self.pasajeros=Vuelo["pasajeros"]