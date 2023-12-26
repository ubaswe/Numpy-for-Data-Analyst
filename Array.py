import numpy as np


#list 
my_list=([1,2,3,4])
(my_list)

#list to array
arr=np.array(my_list)
arr


#matrix 
my_matrix=[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
my_matrix

#matrix to array
arr=np.array(my_matrix)
arr


#tuple
my_tuple=(1,2,3,4)
my_tuple

#tuple to array
arr=np.array(my_tuple)
arr


# In[25]:
#zeros matrix
np.zeros((2,3))


# In[29]:
#one 
np.ones((4,2,),dtype="int32")


# In[30]:
#full Matrix
np.full((5,6),99)


# In[31]:
#rand
np.random.rand(4,2)


# In[45]:
#randint
print(np.random.randint(1,100,10))


# In[46]:
#randint
np.random.randint(-4,8,size=(3,3))


# In[38]:
#randn
np.random.randn(20)


# In[49]:


np.random.randn(30)

