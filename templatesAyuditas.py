#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[97]:


x= np.linspace (0,np.pi*3, 1000)

def seno(x):
    return np.sin(x)
f=seno(x)
plt.plot(x,f)
plt.grid()


# In[19]:


#Derivacion sencilla en caso de necesitarla
df = np.gradient(f)

#De esa forma se pierda siempre un punto 

plt.plot(x,df)
plt.grid()


# In[29]:


#Integracion sencilla en caso de necesitarla
integral = np.trapz(f,x)
print(integral)


# In[100]:


#Metropolis-Hastings en caso de necesatarlo

# 1.
#Generar lista vacia donde se guardaran los pasos y se inicializa
x_walk = np.empty((0)) 
x_0 = 10.0*np.random.random()
x_walk = np.append(x_walk,x_0)

#2
#Uno va a crear numeros nuevos a partir del anterior y mirar si se ajusta más.
#Para mirar si se ajusta más uno saca el Alpha y mira si mejora o no.
#Si mejora el Alfa lo agregra, sino, le da como una segunda oportunidad. 
#En esa oportunidad si el Beta (un numero random) es mas grande que el alpha pues lo agrega.

sigma= 0.1 #Uno lo elige según la distribución
iteraciones= 1000

for i in range(iteraciones):
    x_prime = np.random.normal(x_walk[i], sigma) 
    alpha = seno(x_prime)/seno(x_walk[i])
    if(alpha>=1.0):
        x_walk  = np.append(x_walk,x_prime)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            x_walk = np.append(x_walk,x_prime)
        else:
            x_walk = np.append(x_walk,x_walk[i])

