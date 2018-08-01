class Sucursal(object):
    idSucursal=None
    nombreS=None
    direccionS=None

    def AgregarSucursal(self,idS,nombre,direccion):
        self.idSucursal=idS
        self.nombreS=nombre
        self.direccionS=direccion

        AgregarSucursal= db.cursor(pymysql.cursors.DictCursor)
        AgregarSucursal.execute("INSERT INTO Sucursal VALUES (NULL,' "+ nombre +" ', " + direccion + ");")

    def BorrarSucursal (self,idSucursal):
        BorrarSucursal= db.cursor()
        BorrarSucursal.execute ("DELETE FROM Sucursal WHERE idCliente = " + idSucursal + ";")