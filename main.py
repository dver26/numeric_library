from methods.trapezis import trapezis_compost, trapezis_simple
from methods.simpson import simpson_compost, simpson_simple
from utils.funcions import *

funcions: list[Funcio] = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

def menu():
    print("1 - f1: f(x) = x")
    print("2 - f2: f(x) = x^2")
    print("3 - f3: f(x) = 3x^2 + 2x + 1")
    print("4 - f4: f(x) = sin(x)")
    print("5 - f5: f(x) = cos(x)")
    print("6 - f6: f(x) = exp(x)")
    print("7 - f7: f(x) = 1 / (1 + x^2)")
    print("8 - f8: f(x) = ln(x)")
    print("9 - f9: f(x) = 1 / x")
    print("10 - f10: f(x) = sqrt(x)")

menu()
while True:
    try:
        opcio = int(input("Selecciona una función (1-10):"))
        if opcio < 1 or opcio > 10:
            raise ValueError("No inclos les opcions")
    except ValueError:
        print("Escriu un numero entre el 1 i el 10")
    else:
        break

funcio = funcions[opcio-1]

while True:
    try:
        a = float(input("Escull l'inici de l'inverval d'integració (a): "))
        b = float(input("Escull el final de l'interval d'integració (b): "))
        comprobar_interval(a, b, opcio)
    except ValueError:
        print("Escriu numeros.")
    except AssertionError as err:
        print(err)
    else:
        break

while True:
    try:
        n = int(input("Escull el nombre de subinvervals en que vols dividir l'interval original: "))
    except ValueError:
        print("Escriu un nombre enter.")
    else:
        break


tol = float(input("Escull la tolerància: "))
print(tol)

v_exacte = funcio.F(b) - funcio.F(a)
print(f"Valor exacte de la integral: {v_exacte}")
valor_trapezis_simple = trapezis_simple(a, b, funcio.f)
valor_simpson_simple = simpson_simple(a, b, funcio.f)
print(f"Valor utilitzant trapezis simple: I = {valor_trapezis_simple}\n"
        f"Valor utillitzant simpson simple: I = {valor_simpson_simple}")

valor_trapezis_compost_antic = None
valor_simpson_compost_antic = None



print("Valors aplicant Trapezis composta: ")
for i in range(2, n+1):
    if i > 2:
        valor_trapezis_compost_antic = valor_trapezis_compost
        valor_simpson_compost_antic = valor_simpson_compost

    valor_trapezis_compost = trapezis_compost(a, b, funcio.f, i)
    valor_simpson_compost = simpson_compost(a, b, funcio.f, i)
    print(f"n = {i} | Trapezis: I = {valor_trapezis_compost} | Error: {abs(valor_trapezis_compost - v_exacte)} | Compost: I = {valor_simpson_compost} | Error: {abs(valor_simpson_compost - v_exacte)} ")
    if i > 2 and (abs(valor_simpson_compost - valor_simpson_compost_antic) < tol or 
                  abs(valor_trapezis_compost - valor_simpson_compost_antic) < tol):
        print(f"La diferència entre el valor per n = {i} i per n = {i-1} ja és menor que la tolerància.")
        break