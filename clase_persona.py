class Personas(object):
    tipo=None
    nombre=None
    apellido=None
    fecha_nac=None
    dni=None

    def AgregarPersona(self,Personas):
        self.tipo=Personas["tipo"]
        self.nombre=Personas["nombre"]
        self.apellido=Personas["apellido"]
        self.fecha_nac=Personas["fechaNacimiento"]
        self.dni=Personas["dni"]

class Pasajero(Personas):
    vip=None
    solicitudes_especiales=None

    def AgregarPasajero(self,Pasajero):
        self.vip=Pasajero["vip"]
        try:
            self.solicitudes_especiales = Pasajero["solicitudesEspeciales"]
        except KeyError:
            pass
class Servicio(Personas):
    def __init__(self):
        self.idiomas= []
        self.aviones_habilitados=[]

    def AgregarServicio(self,Servicio):
        self.idiomas=Servicio["idiomas"]
        self.aviones_habilitados=Servicio["avionesHabilitados"]

class Piloto(Personas):
    aviones_habilitados_piloto=None

    def AgregarPiloto(self,Piloto):
        self.aviones_habilitados_piloto=Piloto["avionesHablitados"]