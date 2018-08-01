from dos import DB

class Cliente(object):
    idCliente=None
    quejas=None
    menu=None
    idSucursal=None

    def AgregarCliente(self,idCliente,queja,menu,sucursal):
        self.idCliente=idCliente
        self.quejas=queja
        self.menu=menu
        self.idSucursal=sucursal

        DB().run("INSERT INTO Clientes VALUES (NULL,' " + queja + " ', " + menu + " ," + sucursal + ");")


    def BorrarCliente(self, idCliente):
        BorrarCliente = db.cursor()
        BorrarCliente.execute ("DELETE FROM Clientes WHERE idCliente = " + idCliente + ";")


        # #falta el adbdeit
        # #pasar al main