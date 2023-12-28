#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

#1-D indexing
array_1d=np.array([-10,-2,0,2,17,106,200])
array_1d


# In[7]:


# 0 no index
array_1d[0]


# In[8]:


# 1 no index
array_1d[1]


# In[11]:


# -4 no index
array_1d[-4]


# In[12]:


#index all avlue
array_1d[:]


# In[16]:


#index 0 to 1
array_1d[:2]


# In[17]:


#index 0 to 2
array_1d[0:3]


# In[19]:


# index all value but set size 2
array_1d[::2]


# # 1D Slicing
# 
# 

# In[20]:


array_1d


# In[21]:


array_1d[:2],array_1d[2:]


# In[23]:


array_1d[0]=-102
array_1d


# In[ ]:




