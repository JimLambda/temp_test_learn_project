from time import sleep

from sympy import symbols, diff

x, y = symbols('x, y')

def func0(x, y):
    return ((x ** 0.7) * (y ** 0.3))

def func1(x, y):
    return diff(func0(x,y), x)

print(func1(x,y))

def func2(x, y):
    return diff(func1(x,y), x)

print(func2(x,y))
