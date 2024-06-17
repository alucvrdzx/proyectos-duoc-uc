import os
import msvcrt
import time


def menu():
    print("Welcome to the calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")


def suma():
    num1=float(input("ingrese el primer numero:"))
    num2=float(input("ingrese el segundo numero:"))
    print("el resultado es:",num1+num2)

def resta():
    num1=float(input("ingrese el primer numero:"))
    num2=float(input("ingrese el segundo numero:"))
    print("el resultado es:",num1-num2)

def multiplicacion():
    num1=float(input("ingrese el primer numero:"))
    num2=float(input("ingrese el segundo numero:"))
    print("el resultado es:",num1*num2)

def divicion():
    num1=float(input("ingrese el primer numero:"))
    num2=float(input("ingrese el segundo numero:"))
    if num2!=0:
        print("el resultado es:",num1/num2)
    else:
        print("no se puede dividir entre cero")


while True:
    os.system('cls')
    menu()
    op=int(input("seleccione la opcion que desee: "))
    if op == 1:
        os.system("cls")
        suma()
        print("precione cualquier tecla para continuar...")
        msvcrt.getch()
    elif op == 2:
        os.system("cls")
        resta()
        print("precione cualquier tecla para continuar...")
        msvcrt.getch()
    elif op == 3:
        os.system("cls")
        multiplicacion()
        print("precione cualquier tecla para continuar...")
        msvcrt.getch()
    elif op == 4:
        os.system("cls")
        divicion()
        print("precione cualquier tecla para continuar...")
        msvcrt.getch()
    elif op == 5:
        os.system("cls")
        print("saliendo")
        break
    else:
        print("opcion no valida")
