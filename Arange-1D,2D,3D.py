#!/usr/bin/env python
# coding: utf-8

# In[2]:


#arange
import numpy as np
np.arange(100)


# In[13]:


np.arange(3,10,2)


# In[4]:


np.arange(1,100,5)


# In[14]:


np.arange(2,90,2 ,dtype=float)


# In[38]:


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




