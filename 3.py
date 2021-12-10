import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
from scipy import integrate
import sympy
from scipy import linalg as la
sympy.init_printing()

f = lambda x: 3 + x + x**2 + x**3 + x**4
a, b = -1.0, 1.0
quad_val, err =integrate.quad(f,a,b)
fig, ax = plt.subplots(3,2,figsize = (20,30))

x = np.linspace(-1.2,1.2,1000)
x_2 = np.linspace(a,b,1000)

ax[0][0].plot(x,f(x),lw=2)
ax[0][0].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[0][0].set_title('Trapezoid rule',pad=10,fontsize=20)
ax[0][1].plot(x,f(x),lw=2)
ax[0][1].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[0][1].set_title('Trapezoid rule',pad=10,fontsize=20)
ax[1][0].plot(x,f(x),lw=2)
ax[1][0].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[1][0].set_title('Simpson rule',pad=10,fontsize=20)
ax[1][1].plot(x,f(x),lw=2)
ax[1][1].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[1][1].set_title('Simpson rule',pad=10,fontsize=20)
ax[2][0].plot(x,f(x),lw=2)
ax[2][0].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[2][0].set_title('Mid-point rule',pad=10,fontsize=20)
ax[2][1].plot(x,f(x),lw=2)
ax[2][1].fill_between(x_2,f(x_2),color='green',alpha=0.3)
ax[2][1].set_title('Mid-point rule',pad=10,fontsize=20)


k2,k3=2,5
x2 = np.linspace(a,b,k2)
x3 = np.linspace(a,b,k3)
before_x = -2
before_y = 0
trapz_sumf_2,simp_sumf_2,midp_sumf_2,trapz_sumf_5,simp_sumf_5,midp_sumf_5 = 0,0,0,0,0,0
'''
점이 2개일 때
'''
for inner_x in x2:
    
    t_x = inner_x.astype(float)    
    #사다리꼴 법칙
    ax[0][0].plot(t_x,f(t_x),'ko')    
    ax[0][0].plot([t_x,t_x],[0,f(t_x)],color='r',ls='-')    
    
    if before_x != -2:
        ax[0][0].plot([before_x,t_x],[0,0],color='r',ls='-')
        ax[0][0].plot([before_x,t_x],[f(before_x),f(t_x)],color='r',ls='-')
        trapz_sumf_2 = trapz_sumf_2 + (0.5 * (f(before_x)+f(t_x)) * (t_x - before_x))
    #사다리꼴 법칙 끝
    
    #심프슨의 법칙
    ax[1][0].plot([t_x,t_x],[0,f(t_x)],color='r',ls='-')    
    ax[1][0].plot(t_x,f(t_x),'ko')        
    if before_x != -2:
        
        ax[1][0].plot([before_x,t_x],[0,0],color='r',ls='-')
        simp_sumf_2 = simp_sumf_2 + ((t_x-before_x)/6 * (f(before_x)+4*f((before_x+t_x)/2)+f(t_x)))
    #심프슨의 법칙 끝
    
    #중간점 법칙

    if before_x != -2:

        ax[2][0].plot((before_x+t_x)/2,f((before_x+t_x)/2),'ko')
        ax[2][0].plot([before_x,t_x],[f((before_x+t_x)/2),f((before_x+t_x)/2)],color='r',ls='-')#가로

        ax[2][0].plot([before_x,before_x],[f((before_x+t_x)/2),0],color='r',ls='-')#세로
        ax[2][0].plot([t_x,t_x],[f((before_x+t_x)/2),0],color='r',ls='-')#세로
        midp_sumf_2 = midp_sumf_2 + (t_x-before_x)*f((before_x+t_x)/2)
    #중간점 법칙 끝
    
    before_x = t_x
    
before_x = -2
before_y = 0    
'''
점이 5개일 때
'''
for inner_x in x3:
    
    t_x = inner_x.astype(float)
    
    #사다리꼴 법칙
    ax[0][1].plot(t_x,f(t_x),'ko')    
    ax[0][1].plot([t_x,t_x],[0,f(t_x)],color='r',ls='-')    
    
    if before_x != -2:
        ax[0][1].plot([before_x,t_x],[0,0],color='r',ls='-')
        ax[0][1].plot([before_x,t_x],[f(before_x),f(t_x)],color='r',ls='-')
        trapz_sumf_5 = trapz_sumf_5 + (0.5 * (f(before_x)+f(t_x)) * (t_x - before_x))
    #사다리꼴 법칙 끝
    
    #심프슨의 법칙
    ax[1][1].plot([t_x,t_x],[0,f(t_x)],color='r',ls='-')   
    ax[1][1].plot(t_x,f(t_x),'ko')
            
    if before_x != -2:
        ax[1][1].plot([before_x,t_x],[0,0],color='r',ls='-')
        simp_sumf_5 = simp_sumf_5 + ((t_x-before_x)/6 * (f(before_x)+4*f((before_x+t_x)/2)+f(t_x)))
    #심프슨의 법칙 끝
    
    #중간점 법칙
    if before_x != -2:

        ax[2][1].plot((before_x+t_x)/2,f((before_x+t_x)/2),'ko')
        ax[2][1].plot([before_x,t_x],[f((before_x+t_x)/2),f((before_x+t_x)/2)],color='r',ls='-')#가로

        ax[2][1].plot([before_x,before_x],[f((before_x+t_x)/2),0],color='r',ls='-')#세로
        ax[2][1].plot([t_x,t_x],[f((before_x+t_x)/2),0],color='r',ls='-')#세로
        midp_sumf_5 = midp_sumf_5 + (t_x-before_x)*f((before_x+t_x)/2)
    #중간점 법칙 끝
    
    before_x = t_x

print("quad 함수: %f" % quad_val)   
print("사다리꼴 법칙-점2개: %f, 점5개: %f" %(trapz_sumf_2, trapz_sumf_5))
print("심프슨 법칙-점2개: %f, 점5개: %f" %(simp_sumf_2, simp_sumf_5))
print("중간점 법칙-점2개: %f, 점5개: %f" %(midp_sumf_2, midp_sumf_5))
