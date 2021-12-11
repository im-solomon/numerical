from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt
colors = ['r', 'g', 'b']
idx=0
#연랍방정식
def f(x):
    return [x[0]**3 - 9*x[0] + 3-x[1],np.cosh(0.7*x[0])-x[1]]
#원래 식
f1 = x**3 - 9*x + 3
f2 = np.cosh(0.7*x)
fig, ax = plt.subplots(figsize=(16,3))

#적당한 초기값 지정
x_guesses = [[-3,0],[0,0],[3,0]]
for x_guess in x_guesses:
    #연립방정식으로 해 찾기
    sol = optimize.fsolve(f,x_guess)
    ax.plot(sol[0],sol[1],colors[idx]+'*',markersize=15)
    ax.plot(x_guess[0], x_guess[1], 'ko')
    ax.annotate("", xy = (sol[0], sol[1]), xytext = (x_guess[0],x_guess[1]), arrowprops = dict(arrowstyle = "->",linewidth = 1))
    idx+=1
idx=0
#원래 식으로 그래프 그리기
ax.plot(x,f1,lw=2,label="$x^3 - 9x + 3$")
ax.plot(x,f2,lw=2,label="cosh(0.7x)")
ax.legend(loc=0)
