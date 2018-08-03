from dos import DB
class Sucursal(object):
    idSucursal=None
    nombreS=None
    direccionS=None

    def AgregarSucursal(self,idS,nombre,direccion):
        self.idSucursal=idS
        self.nombreS=nombre
        self.direccionS=direccion

        AgregarSucursal= DB.cursor(pymysql.cursors.DictCursor)
        AgregarSucursal.execute("INSERT INTO Sucursal VALUES (NULL,' "+ nombre +" ', " + direccion + ");")

    def BorrarSucursal (self,idSucursal):
        BorrarSucursal= DB.cursor()
        BorrarSucursal.execute ("DELETE FROM Sucursal WHERE idCliente = " + idSucursal + ";")

    def DeserializarSucursal(self, DicSucursal ):
        self.idSucursal= DicSucursal["idSucursal"]
        self.nombreS= DicSucursal["nombreS"]
        self.direccionS= DicSucursal["direccionS"]