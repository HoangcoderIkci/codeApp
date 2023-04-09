
import sympy as sp
import numpy as np
from fractions import Fraction
import fuldamentalsystem as fusr
x = sp.symbols('x')
A = sp.Matrix([[2,-1,2],
              [2,2,-1],
              [-1,2,2]])
A*=1/3
A_coppy = sp.Matrix(A)
for i in range(3):
    A[i,i] -= x
A_coppy = A_coppy**2 - A_coppy + sp.diag(1,1,1)
#print(A_coppy)
solution = fusr.solve_homogeneous_system(A_coppy)
print(solution)

