import sympy as sp
from scipy import optimize
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x1data,x2data, ydata=np.loadtxt("data_3.text", unpack = True)

def f(X,a0,a1,a2,a3):
    x1,x2=X
    return a0 + a1*x1 + a2*x2 + a3*x1*x2

def g(alpha):
    return ydata - f([x1data,x2data], *alpha)

alpha_start = (1,1,1,1)
alpha_opt, alpha_cov = optimize.leastsq(g, alpha_start)

print("계수 a0: %f, a1:%f, a2:%f,a3: %f"% (alpha_opt[0], alpha_opt[1],alpha_opt[2],alpha_opt[3]))
x_ = y_ = np.linspace(-25,25, 1001)
X_, Y_ = np.meshgrid(x_, y_)

fig, ax = plt.subplots(figsize = (8, 4))

c=ax.contourf(X_,Y_,f([X_,Y_],*alpha_opt), cmap='jet', levels=15)
ax.contour(X_,Y_,f([X_,Y_],*alpha_opt), linewidths=0.5, colors='k', levels=15)
plt.colorbar(c)
