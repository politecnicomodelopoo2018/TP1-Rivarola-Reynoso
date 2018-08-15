
import pymysql
from dos import DB
from claseCliente import Cliente
from claseMenu import Menu
from claseEmpleado import Empleado
from claseSucursal import Sucursal
from menu import Menuu
DB().SetConection('127.0.0.1', 'root', 'alumno', 'mydb')



Cliente = Cliente()
Menu= Menu()
Empleado=Empleado()
Sucursal=Sucursal()

menu=Menuu()
variable = input("Id sucursal")
Sucursal.BorrarSucursal(variable)

#claseSucursal = Sucursal.AgregarSucursal(None, "Pueyrrdn", "cramer 4567")


#claseMenu= Menu.borrarMenu(1)

menuesss = Menuu.MenuMenu()