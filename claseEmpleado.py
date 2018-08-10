from dos import DB
class Empleado(object):
    idEmpleado=None
    nombreEmpleado=None
    apellidoEmpleado=None
    DNIempleado=None
    idSucursal=None


    def AgregarEmpleado(self, idE, nombreE,apellidoE,DNIE,IDsucursal):
            self.idEmpleado = idE
            self.nombreEmpleado = nombreE
            self.apellidoEmpleado = apellidoE
            self.DNIempleado=DNIE
            self.idSucursal=IDsucursal


            AgregarSucursal = DB.cursor(pymysql.cursors.DictCursor)
            AgregarSucursal.execute("INSERT INTO Empleados VALUES (NULL,' " + nombreE + " ', '" + apellidoE + "', '"+DNIE+ "','"+IDsucursal+"');")



    def BorrarEmpleado(self,idEmpleado):
        BorrarEmpleado= DB.cursor(pymysql.cursors.DictCursor)
        BorrarEmpleado.execute("DELETE FROM Empleados WHERE idEmpleado = " + idEmpleado + ";")

    def DeserializarEmpleado(self, DicEmpleado):
        self.idEmpleado= DicEmpleado["idEmpleado"]
        self.nombreEmpleado=DicEmpleado["nombreEmpleado"]
        self.apellidoEmpleado=DicEmpleado["apellidoEmpleado"]
        self.DNIempleado=DicEmpleado["DNIempleado"]
        self.idSucursal=DicEmpleado["idSucursal"]


       







