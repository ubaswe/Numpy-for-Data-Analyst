
#arange
import numpy as np
#0 to 100
np.arange(100)


# In[13]:lower limit 3 upper limit 10 and gap 2.
np.arange(3,10,2)


# In[4]:
np.arange(1,100,5)

# In[14]:
np.arange(2,90,2 ,dtype=float)


# In[14]:linspace function lower limit 1 upper limit 10 and 100 means divion
np.linspace(1,10,100)

np.linspace(1,10,100,)

# In[38]:lower limit 1 upper limit 14 and 100 pieces,retstep=True will show the differance of piece

np.linspace(1,15,100,retstep=True)


#1-D array
x=np.arange(0,16)
x


# In[39]:


x.shape


# In[43]:


#2-D array
x.reshape(4,4)


# In[45]:


#3-D array
x.reshape(4,2,2)


# In[46]:


#1-D convert
x.reshape(1,16)


# In[ ]:




