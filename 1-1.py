from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt
#x가 표현되는 범위 -4 ~ 4
x = np.arange(-4,5,0.01)
f1 = x**3 - 9*x + 3
f2=np.cosh(0.7*x)
fig, ax = plt.subplots(figsize=(16,3))

#두 식의 그래프 표현
ax.plot(x,f1,lw=2,label="$x^3 - 9x + 3$")
ax.plot(x,f2,lw=2,label="cosh(0.7x)")
ax.set_xlabel('$x$',fontsize=18)
ax.legend()


