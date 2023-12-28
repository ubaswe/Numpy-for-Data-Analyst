#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
array_2d= np.arange(24)
array_2d.shape = (6,4)
array_2d


# In[13]:


#2-D indexing
array_2d[2]


# In[15]:


#[[]] to print row
array_2d[[2,3,4]]


# In[16]:


#row no 5 colum 2
array_2d[5,2]


# In[17]:


#: is used for range.) to 1 range row and 0 to 1 range column
array_2d[:2,:2]


# In[22]:


#: is used for range.) to 3 range row and 0 to 1 range column
array_2d[:4,:2]


# In[24]:


array_2d[:,[2]]


# In[ ]:




