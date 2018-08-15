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


           DB().run("INSERT INTO Empleados VALUES (NULL,' " + nombreE + " ', '" + apellidoE + "', '"+DNIE+ "','"+IDsucursal+"');")

    def BorrarEmpleado(self,idEmpleado):
       DB().run("DELETE FROM Empleados WHERE idEmpleado = " + idEmpleado + ";")

    def UpdateEmpleado(idCliente):
        DB().run("update Empleado set idEmpleado= "+idEmpleado+", nombreEmpleado= "+nombreEmpleado+",apellidoEmpleado= "+apellidoEmpleado+",dniEmpleado="+dniEmpleado+",idSucursal="+idSucursal+")

    def DeserializarEmpleado(self, DicEmpleado):
        self.idEmpleado= DicEmpleado["idEmpleado"]
        self.nombreEmpleado=DicEmpleado["nombreEmpleado"]
        self.apellidoEmpleado=DicEmpleado["apellidoEmpleado"]
        self.DNIempleado=DicEmpleado["DNIempleado"]
        self.idSucursal=DicEmpleado["idSucursal"]


       







