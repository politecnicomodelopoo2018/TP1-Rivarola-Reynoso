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

        DB.run("INSERT INTO Menues VALUES (NULL,' "+ nombre +" ', " + precioMenu + " ,"  +tipoMenu+");")

    def borrarMenu(self,idMenu):
        BorrarMenu= db.cursor()
        BorrarMenu.execute ("DELETE FROM Menues WHERE idMenues = " + idMenu + ";")

    #falta el adbdeit