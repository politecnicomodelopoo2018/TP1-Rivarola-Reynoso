from dos import DB
from claseCliente import Cliente
from claseMenu import Menu
from claseEmpleado import Empleado
from claseSucursal import Sucursal

dos=DB()
cliente=Cliente()
menu=Menu()
empleado=Empleado()
Sucursal=Sucursal()

class Menu(object):
    opcion=None

    def MenuMenu(self,opcion):

        opcion =input("OPCIONES DEL CLIENTE: ")
        opcion =input("1) Agregar un cliente")
        opcion =input("2) Borrar un clinte")
        input("3) Modificar un cliente")

        input("OPCIONES DEL MENU:")
        input("4)Agregar un menu")
        input("5)Borrar un menu")
        input("6)Modificar un menu")

        input("OPCIONES DEL EMPLEADO: ")
        input("7) Agregar un empleado")
        input("8) Borrar un empleado")
        input("9) Modificas un empleado")

        input("OPCIONES DE SUCURSAL: ")
        input("1) Agregar una sucursal")
        input("2) Borrar un menu")
        input("3) Modificar un menu")

