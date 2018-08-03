
# import pymysql


from dos import DB
from claseCliente import Cliente
from claseMenu import Menu
from claseEmpleado import Empleado
from claseSucursal import Sucursal

Cliente = Cliente()
Menu= Menu()
Empleado=Empleado()
Sucursal=Sucursal()
db = DB()


#claseSucursal = Sucursal.AgregarSucursal(None, "Pueyrrdn", "cramer 4567")


claseMenu= Menu.borrarMenu(1)