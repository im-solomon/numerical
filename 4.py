import sympy as sp
from scipy import optimize
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#원래 함수
def f(x, m, v):
    return 1/(np.sqrt(2*np.pi*v)) * np.exp(-(x-m)**2/2*v)

xdata,ydata = np.loadtxt("data_1.text", unpack = True)
#오류함수
def g(alpha):
    return ydata - f(xdata, *alpha)
#시작 값
alpha_start = (1,1)
#계수 찾기
alpha_opt, alpha_cov = optimize.leastsq(g, alpha_start)
x = np.linspace(-5, 5, 100)
fig, ax = plt.subplots(figsize = (8, 4))
#찾은 계수 값을 포함한 방정식으로 그래프 그리기
ax.plot(x, f(x,*alpha_opt), lw = 3, alpha = 0.5, label = 'Model')
#원 데이터
ax.scatter(xdata, ydata, label = 'Data',color='r', marker = '.')

ax.set_xlabel('$x$', fontsize = 18)
ax.set_ylabel(r'$f(x)$', labelpad = 30, fontsize = 18, rotation = 0, )
ax.legend()
ax.grid()
print("m: %f, 𝜎^2: %f"%(alpha_opt[0],alpha_opt[1]))
