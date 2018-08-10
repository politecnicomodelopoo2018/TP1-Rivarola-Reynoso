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
            AgregarCliente(None,"muy sucio","Cuarto de libra",1)
        elif opcion == "2":
            BorrarCliente(1)
        elif opcion== "3":

        elif opcion== "4":
            AgregarMenu(None,"Cuarto de libra","345",None)
        elif opcion== "5":
            BorrarMenu(3)
        elif opcion=="6":

        elif opcion=="7":
           AgregarEmpleado(None,"Juan","Perez","43018547",1)
        elif opcion=="8":
           BorrarEmpleado(2)
        elif opcion=="9":

        elif opcion=="10":
           AgregarSucursal(None,"DEvto","AV.josejha.com ahre ")
        elif opcion=="11":
            BorrarSucursal(3)
        elif opcion=="12":


