import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sympy
sympy.init_printing()
import mpmath

x = sympy.symbols("x")
f = x**4 +3*x**3 - 2*x**2 - 3*x + 1
#해석적인 적분
sympy.integrate(f,(x,0,1))

sympy.N(_)
#수치적인 적분
f2 = sympy.lambdify(x,f)
scipy.integrate.quad(f2,0,1)

#소수점 100자리
mpmath.mp.dps = 100
f3 = sympy.lambdify(x,f,'mpmath')
val = mpmath.quad(f3,(0,1))
sympy.sympify(val)
