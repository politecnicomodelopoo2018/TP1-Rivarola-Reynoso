from dos import DB
from claseCliente import Cliente
from claseMenu import Menu
from claseEmpleado import Empleado
from claseSucursal import Sucursal

Cliente = Cliente()
Menu= Menu()
Empleado=Empleado()
Sucursal=Sucursal()
DB= DB()

claseSucursal = Sucursal.AgregarSucursal(None, "Pueyrredn", "cramer 4567")