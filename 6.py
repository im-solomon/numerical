import sympy as sp
from scipy import optimize
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import interpolate
from numpy import polynomial as P
from scipy import linalg

data= np.load('data_2.npy')
np.savetxt("save.txt", data, fmt='%f')
xdata,ydata= np.loadtxt('save.txt', unpack = True)

#체비세프 다항식
B = P.chebyshev.chebvander(xdata, 10)
d = linalg.solve(B, ydata) 
f2 = P.Chebyshev(d)

#3차 운형 곡선
f_i = interpolate.interp1d(xdata,ydata, kind = 3)

xx = np.linspace(-2, 2, 301)
fig, ax = plt.subplots(figsize = (8, 4))
#원래 점 표시
ax.scatter(xdata,ydata,100, label = 'Data',color='b', marker = '.') 
#3차 운형 곡선 표시
ax.plot(xx, f_i(xx), 'r--', label = 'Cubic spline')
#체비세프 다항식 표시
ax.plot(xx, f2(xx), 'k', lw = 2, label = 'Chebyshev basis', alpha = 0.5)
ax.legend()
