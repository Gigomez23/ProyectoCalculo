import numpy as py
from scipy.optimize import fsolve
from sympy import sympify, symbols, lambdify

def ejeEnAxis():
    eje = str(input("El eje es en x o y"))
    if (eje == 'y'):
        return False
    else:
        return True

def eje(eje):
    if eje == True:
        eje = input("Digite el eje de x = ")
    else:
        eje = input("Digite el eje de y = ")
    return eje

def get_function_from_input(prompt, eje):
    if eje == True:
        user_input = input(prompt)
        x = symbols('x')
        parsed_function = sympify(user_input)
        return lambdify(x, parsed_function)

