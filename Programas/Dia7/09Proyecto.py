from random import randint
from os import system

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cueta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""Nombre de cliente: {self.nombre} {self.apellido}
                Numero de cuenta: {self.numero_cueta}
                saldo: $ {self.balance} MXN\n"""
    def depositar(self,deposito):
        self.balance = self.balance + deposito
        print(f"Su saldo ahora es de ${self.balance} MXN")

    def retiro(self,retiro):
        if retiro > self.balance:
            print(f"Saldo insuficiente. Trate nuevamente\n")
            return False
        else:
            self.balance = self.balance - retiro
            print(f"Su saldo ahora es de ${self.balance} MXN")
            return True

def crear_cliente():
    nombre = input("Ingrese su(s) nombre(s): ")
    apellido = input("Ingrese su(s) apellidos(s): ")
    numero_cuenta = '1900' + '8000' + str(randint(1,9)) +  str(randint(1,9))

    return Cliente(nombre,apellido,numero_cuenta,0)

def inicio():
    opc = 'x'
    finalizar_programa = False

    cliente = crear_cliente()
    while not finalizar_programa:
        while not opc.isnumeric() or int(opc) not in range(1,4):
            system('cls')
            print(cliente)
            print('''\nElige una opción: \n
                    1. Depositar.
                    2. Retirar.
                    3. Salir.\n''')

            opc = input("Opción: ")

        if opc == '1':
            deposito = float(input("Cantidad a depositar: "))
            cliente.depositar(deposito)
            opc=volver_inicio()
        elif opc =='2':
            band = False
            while band == False:
                retiro = float(input("Cantidad a retirar: "))
                band = cliente.retiro(retiro)
            opc=volver_inicio()
        else:
            finalizar_programa = True

def volver_inicio():
    opc = 'x'
    while opc != 'v':
        print('\nPresione "v" para volver al menú inicial.')

        opc = input("Opción: ").lower()
    return 'x'
inicio()