from sympy import *

x = symbols("x")
y = symbols("y")

formula = sin(x**2+1)

print(diff(formula))