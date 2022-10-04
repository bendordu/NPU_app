#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[136]:


gsr = pd.read_csv('C:/Users/darya/Desktop/results/gsr.csv', header=1)
gsr


# In[54]:


# fig = plt.figure(figsize=(200, 50))
plt.plot(gsr["GSR(Om)"])


# In[137]:


raw = pd.read_csv('C:/Users/darya/Desktop/results/raw.csv', header=1)
raw


# In[145]:


# fig = plt.figure(figsize=(50, 200))
plt.plot(raw["GSR(Om)"])

plt.plot(gsr["GSR(Om)"])


# In[141]:


# fig = plt.figure(figsize=(200, 50))
plt.plot(raw["EMG"])

plt.plot(gsr["EMG"])


# In[154]:


ind = 0
diii = []

while ind < raw["EMG"].count():

    first = raw["EMG"].iloc[ind:(ind + 27)].tolist()

    n = 0
    dif = 0

    while n < len(first)-1:
        j = abs((first[n+1] - first[n]) / 0.1)
        dif += j
        n += 1
        
    diii += [dif]
    ind += 27
    
print(diii)

# от 500 до 1500


# In[138]:


emg = pd.read_csv('C:/Users/darya/Desktop/results/emgend.csv', header=1)
emg


# In[132]:


# fig = plt.figure(figsize=(200, 200))
plt.plot(emg["EMG"])


# In[116]:


# first = emg["EMG"].iloc[:27].tolist()

# n = 0
# dif = 0

# while n < len(first)-1:
#     j = abs((first[n+1] - first[n]) / 0.1)
#     dif += j
#     n += 1
    
# print(dif)


# In[151]:


ind = 0
difff = []

while ind < emg["EMG"].count():

    first = emg["EMG"].iloc[ind:(ind + 27)].tolist()

    n = 0
    dif = 0

    while n < len(first)-1:
        j = abs((first[n+1] - first[n]) / 0.1)
        dif += j
        n += 1
        
    difff += [dif]
    ind += 27
    
print(difff)

# у первой части сотни, у второй - десятки тысяч


# In[139]:


emg_noise = pd.read_csv('C:/Users/darya/Desktop/results/noiseemg.csv', header=1)
emg_noise


# In[65]:


# fig = plt.figure(figsize=(200, 50))
plt.plot(emg_noise["EMG"])


# In[140]:


emg1 = pd.read_csv('C:/Users/darya/Desktop/results/emg1.csv', header=1)
emg1


# In[67]:


plt.plot(emg1["EMG"])


# In[149]:


plt.plot(emg["EMG"])

plt.plot(raw["EMG"])

plt.plot(gsr["EMG"])


# In[160]:


fig = plt.figure(figsize=(100, 100))
plt.plot(difff)
plt.plot(diii)


# In[163]:


plt.plot(diii)
plt.plot(difff[46:])


# In[162]:


plt.plot(difff)


# In[ ]:




