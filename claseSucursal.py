from dos import DB
class Sucursal(object):
    idSucursal=None
    nombreS=None
    direccionS=None

    def AgregarSucursal(self,idS,nombre,direccion):
        self.idSucursal=idS
        self.nombreS=nombre
        self.direccionS=direccion

        DB().run("INSERT INTO Sucursal VALUES (NULL,'"+ self.nombreS +"', '" + self.direccionS + "');")

    def BorrarSucursal (self,idSucursal):
        DB().run("DELETE FROM Sucursal WHERE idCliente = " + idSucursal + ";")

    def UpdateSucursal(self):
        DB().run("update Sucursal set idSucursal= "+self.idCliente+", nombreS= " + self.nombreS + ",direccionS= " + self.direccionS+";")

    def DeserializarSucursal(self, DicSucursal ):
        self.idSucursal= DicSucursal["idSucursal"]
        self.nombreS= DicSucursal["nombreS"]
        self.direccionS= DicSucursal["direccionS"]