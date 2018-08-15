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

class Menuu(object):
    opcion=None

    def MenuMenu(self):

        print("OPCIONES DEL CLIENTE: ")
        print("1) Agregar un cliente")
        print("2) Borrar un clinte")
        print("3) Modificar un cliente")

        print("OPCIONES DEL MENU:")
        print("4)Agregar un menu")
        print("5)Borrar un menu")
        print("6)Modificar un menu")

        print("OPCIONES DEL EMPLEADO: ")
        print("7) Agregar un empleado")
        print("8) Borrar un empleado")
        print("9) Modificas un empleado")

        print("OPCIONES DE SUCURSAL: ")
        print("10) Agregar una sucursal")
        print("11) Borrar un menu")
        print("12) Modificar un menu")

        opcion=input("Inserte su opcion")

        if opcion == "1":
            cliente.AgregarCliente(None,"muy sucio","Cuarto de libra",1)
        if opcion == "2":
            Cliente.BorrarCliente(1)
        if opcion== "3":

        if opcion== "4":
            Menu.AgregarMenu(None,"Cuarto de libra","345",None)
        if opcion== "5":
            Menu.BorrarMenu(3)
        if opcion=="6":

        if opcion=="7":
           Empleado.AgregarEmpleado(None,"Juan","Perez","43018547",1)
        if opcion=="8":
            Empleado.BorrarEmpleado(2)
        if opcion=="9":

        if opcion=="10":
           Sucursal.AgregarSucursal(None,"DEvto","AV.josejha.com ahre ")
        if opcion=="11":
            Sucursal.BorrarSucursal(3)
        if opcion=="12":


