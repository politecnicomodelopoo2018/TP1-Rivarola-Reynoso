from dos import DB

class Cliente(object):
    idCliente=None
    quejas=None
    menu=None
    idSucursal=None

    def AgregarCliente(self,id,queja,menu,sucursal):
        self.idCliente=id
        self.quejas=queja
        self.menu=menu
        self.idSucursal=sucursal

    def InsertCliente(self,idC,queja,menu,sucursal):
        Agregarcliente = db.cursor()
        Agregarcliente.execute ("INSERT INTO Clientes VALUES (NULL,' " + idC + "', ' "+ queja +" ', " + menu + " ,"  +sucursal+");")