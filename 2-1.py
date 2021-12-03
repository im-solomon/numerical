import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sympy
sympy.init_printing()

x = sympy.symbols("x")
f = x**4 +3*x**3 - 2*x**2 - 3*x + 1
sympy.integrate(f,(x,0,1))

sympy.N(_)

f = sympy.lambdify(x,f)
scipy.integrate.quad(f,0,1)
