class Avion(object):
    codigo=None
    cantidadPasajerosMaxima=None
    cantidadTripulacionNecesaria= None

    def AgregarAvion(self,Avion):
        self.codigo= Avion ["codigoUnico"]
        self.cantidadPasajerosMaxima= Avion["cantidadDePasajerosMaxima"]
        self.cantidadTripulacionNecesaria = Avion["cantidadDeTripulaciónNecesaria"]

