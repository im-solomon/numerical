from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt

#해석적인 방법
#첫번째 방정을 자코비 행렬로 해찾기
x,y = sympy.symbols("x,y")
f_mat = sympy.Matrix([x**3 - 9*x + 3-y])
f_mat.jacobian(sympy.Matrix([x,y]))

#두번째 방정을 자코비안으로 해찾기
f_mat = sympy.Matrix([sympy.cosh(0.7*x)-y])
f_mat.jacobian(sympy.Matrix([x,y]))

#두 연립방정식을 자코비안으로 해 찾기
f_mat = sympy.Matrix([x**3 - 9*x + 3-y, sympy.cosh(0.7*x)-y])
f_mat.jacobian(sympy.Matrix([x,y]))

#수치적인 방법으로 해찾기
def f_jacobian(x):
    return [[3*x[0]**2 - 9,-1],[0.7 * np.sinh(0.7 * x[0]),-1]]
optimize.fsolve(f,[0,0],fprime = f_jacobian)
