#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np

#1-D zeros and float
np.zeros(16)


# In[24]:


#2-D zeros that's why two (()) and float
np.zeros((4,4))


# In[34]:


#3-D zeros and coverted to int
np.zeros((4,4,4),dtype="int32")


# In[ ]:





# In[35]:


#1-D one that's why one ()
np.ones(4)


# In[38]:


#3-D one that's why one (())
np.ones((4,4,4),dtype="int32")


# In[39]:


#Full
np.full((4,4),99)


# In[45]:


np.full((6,3),77)


# In[41]:


#rand is o to 1 random array but float
np.random.rand(4,2)


# In[44]:


np.random.rand(6,5)


# In[47]:


#randit is int 1 is lower limt 100 is upper limit and quantity=10
np.random.randint(1,100,10)


# In[51]:


##randit is int -1 is lower limt 8 is upper limit and size 
np.random.randint(-1,8, size=(3,3))


# In[52]:


#randn
np.random.randn(20)


# In[53]:


np.random.random(50)


# In[ ]:




