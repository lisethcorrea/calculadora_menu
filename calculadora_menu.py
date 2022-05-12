# calculadora basica con menu

from __future__ import print_function
from math import log
from operator import truediv
from sys import _enablelegacywindowsfsencoding

# input
bandera = False
x = float(input("dame el valor del numero x: "))
y = float(input("dame el valor del numero y:"))

print("dame la opcion que deseas realizar: \n")

# se despliega el menu para seleccionar la opcion que deseas realizar
print("1. sumar")
print("2 restar")
print("3. multiplicar")
print("4. dividir")
print("5. potencia")
print("6. logaritmo")

opcion = int(input("dame la opcion: "))

# processing
if (opcion ==1):
    z = x + y
    print(x," + ",y)
elif (opcion ==2):
    z = x - y
    print(x, " - ",y)
elif (opcion == 3):
    z = x * y
    print(x), " * ",y
elif (opcion == 4 and y != 0):
    z = x/y
    print(x, " / ", y)
elif (opcion == 4 and y == 0):
    print("el denominador es igual a cero y ")
    print("no se puede realizar la divicion")
    bandera = True
elif (opcion ==5):
     z = pow(x,y) 
     print(x," ^ ", y)
elif (opcion == 6 and x > 0):
     z = log(x)
     print("logaritmo de ",x)
elif (opcion ==6 and x <= 0):
     print("no se puede calcular el logaritmo.")
     bandera = True
else:
    print("opcion no valida")

# se escribe el resultado con otra condicion
if (opcion < 7 and bandera == False):
    print("resultado =", z)

    # fin     