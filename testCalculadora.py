#testCalculadora.py --- Calculadora aritmetica simple 
import os

# Funciones para la suma y resta de numeros ---

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

# Funciones para la multiplicacion y division de numeros ---

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

# Pausa -------------------------------------------------------------------

def pausa():
    print("Presiona <Enter> para continuar")
    input()

# Suma de dos numeros -----------------------------------------------------

def suma():
    os.system("clear")
    print("SUMA DE DOS NUMEROS")
    print("===================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = sumar(a,b)
    print(f'{a:5.2f} + {b:5.2f} = {c:5.2f}')

    pausa()

# Resta de dos numeros -----------------------------------------------------

def resta():
    os.system("clear")
    print("RESTA DE DOS NUMEROS")
    print("====================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = restar(a,b)
    print(f'{a:5.2f} - {b:5.2f} = {c:5.2f}')
    pausa()

# Multiplicacion dos numeros ------------------------------------------------

def multiplica():
    os.system("clear")
    print("MULTIPLICACION DE DOS NUMEROS")
    print("=============================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = multiplicar(a,b)
    print(f'{a:5.2f} * {b:5.2f} = {c:5.2f}')
    
    pausa()

# División dos numeros ------------------------------------------------

def divide():
    os.system("clear")
    print("DIVISIÓN DE DOS NUMEROS")
    print("=======================")
    a = float(input("A:"))
    b = float(input("B:"))

    c = dividir(a,b)
    print(f'{a:5.2f} / {b:5.2f} = {c:5.2f}')
    pausa()

# Menu principal ----------------------------------------------------------

def menu():
    os.system("clear")
    print("CALCULADORA ARITMETICA")
    print("======================")
    print("1->Sumar")
    print("2->Restar")
    print("3->Multiplicar")
    print("4->Dividir")
    print("*->Salir")
    opcion = input("Opcion->")

    return opcion

def main():
    opcion = "1"
    while opcion != "*":
        opcion = menu()

        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplica()
        elif opcion == "4":
            divide()
        
    os.system("clear")
    print("Fin de la calculadora...")

if __name__=='__main__':
    main()