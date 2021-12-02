#!/usr/bin/env python
# coding: utf-8

# In[33]:


from scipy import linalg as la
from scipy import optimize
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt

x,y = sympy.symbols("x,y")
f_mat = sympy.Matrix([x**3 - 9*x + 3-y])
f_mat.jacobian(sympy.Matrix([x,y]))


# In[37]:


f_mat = sympy.Matrix([sympy.cosh(0.7*x)-y])
f_mat.jacobian(sympy.Matrix([x,y]))


# In[39]:


f_mat = sympy.Matrix([x**3 - 9*x + 3-y, sympy.cosh(0.7*x)-y])
f_mat.jacobian(sympy.Matrix([x,y]))


# In[45]:


def f_jacobian(x):
    return [[3*x[0]**2 - 9,-1],[0.7 * np.sinh(0.7 * x[0]),-1]]
optimize.fsolve(f,[0,0],fprime = f_jacobian)
