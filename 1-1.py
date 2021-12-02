#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import linalg as la


# In[2]:


from scipy import optimize


# In[3]:


import sympy


# In[5]:


sympy.init_printing()


# In[6]:


import numpy as np


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


x = np.arange(-4,4,0.01)


# In[9]:


f1 = x**3 - 9*x + 3


# In[10]:


f2=np.cosh(0.7*x)


# In[15]:


fig, ax = plt.subplots(figsize=(16,3))


# In[16]:


ax.plot(x,f1,lw=2,label="$x^3 - 9x + 3$")


# In[17]:


ax.plot(x,f2,lw=2,label="cosh(0.7x)")


# In[18]:


fig


# In[19]:


ax.set_xlabel('$x$',fontsize=18)


# In[20]:


fig


# In[21]:


ax.legend()


# In[22]:


fig


# In[ ]:




