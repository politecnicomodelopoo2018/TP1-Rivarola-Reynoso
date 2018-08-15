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

         DB().run("INSERT INTO Clientes VALUES (NULL,' " + queja + " ', '" + menu + "' ,'" + sucursal + "');")


    def BorrarCliente(idCliente):
        DB().run("DELETE FROM Clientes WHERE idCliente = " + idCliente + ";")


    def UpdateCliente(idCliente):
        DB().run("update Clientes set idCliente= "+idCliente+", quejas= "+quejas+",menu= "+menu+",idSucursal="+idSucursal+")




    def DeserializarCliente(self, DicCliente):
        self.idCliente= DicCliente["idCliente"]
        self.quejas= DicCliente["quejas"]
        self.menu= DicCliente["menu"]
        self.idSucursal=DicCliente["idSucursal"]
