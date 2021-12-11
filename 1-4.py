from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return [x[0]**3 - 9*x[0] + 3-x[1],np.cosh(0.7*x[0])-x[1]]
x = np.linspace(-4,4,5001)
y1 = x**3 - 9*x + 3
y2 = np.cosh(0.7*x)
fig, ax = plt.subplots(figsize=(8,4))

ax.set_ylim([-20, 20])
ax.plot(x,y1,'b',lw=1.5,label="$x^3 - 9x + 3$")
ax.plot(x,y2,'g',lw=1.5,label="cosh(0.7x)")

#각 점에서의 해 찾기
sol1 = optimize.fsolve(f,[-3,0])
sol2 = optimize.fsolve(f,[0,0])
sol3 = optimize.fsolve(f,[3,0])


colors = ['r','g','b']
#x축 [-4,4]범위에서 100개
for m in np.linspace(-4,4,100):
    #y축 [-15,15]범위에서 50개    
    for n in np.linspace(-15,15,50):
        x_guess = [m,n]
        #총 5000개의 점이 어느 해로 수렴하는지 조사 함
        sol = optimize.fsolve(f,x_guess)
        for idx, s in enumerate([sol1,sol2,sol3]):
            if abs(s-sol).max() <1e-8:
                ax.plot(sol[0], sol[1], colors[idx]+'*',markersize=10)
                ax.plot(x_guess[0],x_guess[1],colors[idx]+'*',markersize=1)
