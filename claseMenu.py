from dos import DB
class Menu(object):
    idMenu=None
    nombre=None
    precioMenu=None
    tipoMenu=None

    def AgregarMenu(self,idM,nombre,precioMenu,tipoMenu):
        self.idMenu=idM
        self.nombre=nombre
        self.precioMenu=precioMenu
        self.tipoMenu=tipoMenu

        DB.run("INSERT INTO Menues VALUES (NULL,' "+ nombre +" ', '" + precioMenu + "' ,'"  +tipoMenu+"');")

    def BorrarMenu(self,idMenu):
        DB.run("DELETE FROM Menues WHERE idMenues = " + idMenu + ";")

    def UpdateMenu(idCliente):
        DB().run("update Menu set idMenu= "+idMenu+", nombre= "+nombre+",precioMenu= "+precioMenu+",tipoMenu="+tipoMenu+")

    def DeserializarMenu(self, DicMenu):
        self.idMenu=DicMenu["idMenu"]
        self.nombre=DicMenu["nombre"]
        self.precioMenu=DicMenu["precioMenu"]
        self.tipoMenu=DicMenu["tipoMenu"]