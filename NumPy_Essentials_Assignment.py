#!/usr/bin/env python
# coding: utf-8

# # NumPy Essentials Practice Exercises Overview:
# Time to test the knowledge on NumPy. Lets start with simple task and move on to more challenging ones!<br>
# **Good Luck**<br>
# 
# &#9758; *Please note, there are several ways to get the required output, so your code could be different then what is provided in this notebook. <br>As long as you are getting the tasks done, it is fine at this stage. *

# **1. What is the major difference between "`Vector`" and "`Matrix`"?**

# In[ ]:


Vector is one dimensional and matrix is two dimensional.


# **2. How to import `NumPy` library?** 

# In[ ]:


import numpy as np


# In[ ]:





# **3. Convert the given Python list into NumPy array and check its data type**

# In[ ]:


list_1 = [1,2,3,4,5]


# In[ ]:


np.array(list_1)


# In[ ]:





# **4. Generate `array [0,1,2,3,4,5]` using NumPy built-in function, `arange()`**

# In[ ]:


np.arange(0,6)


# In[ ]:





# **5. Generate an `array of "5" zeros` **

# In[ ]:


np.zeros(5)


# In[ ]:





# **6. Generate the following `matrix`.**

# In[ ]:


np.zeros((3,4))


# In[ ]:





# **7. Generate** `[1.,1.,1.,1.,1.]` **using NumPy built-in function?**

# In[ ]:


np.ones(5)


# In[ ]:





# **8. Generate an array of "5" tens.**

# In[ ]:


np.full((5,1),10)


# In[ ]:





# **9. Use `arange()` to generate an array of even numbers between 50 and 100.**<br>
# *50 and 100 are not included*

# In[ ]:


np.arange(52,100,2)


# In[ ]:





# **10. Generate an array of 10 linearly spaced points between 0 and 1.**<br>
# **Output step size as well?**

# In[20]:


np.linspace(0,1,10,retstep=True)


# In[ ]:





# **11. Perform the following tasks:**
# * Generate a **`vector array of 25`** numbers using **`arange()`**
# * write a code to convert the vector array into **`2-D matrix using reshape`**
# * can we use **`shape`** instead of reshape as well?

# In[21]:


x=np.arange(25) 


# In[22]:


# Generating vector array


# In[23]:


x.reshape(5,5)


# In[24]:


# reshape to convert into 2-d


# In[25]:


x.shape=(5,5)
x


# In[26]:


# Using shape


# **12. Please generate the following matrix.**

# In[27]:


y=np.arange(0.1,2.6,.1)
y
y.reshape(5,5)


# In[14]:





# **13. Write a code to generate the output below, use "`linspace()`" and "`print()`"**

# In[29]:


# To avoid overwriting the output, please code here 


# In[27]:


x=np.linspace(0,25,25,dtype='int32')
x.shape=(5,5)

print(x)


# **14. What is the main difference between `linspace()` and `arange()`?**

# In[31]:


The main difference  between linspace() and arange() is the way of generate values.
linspace() focuses on generating a specific number of evenly spaced points between two values,
while arange() generates values with a specified step size within a given range.


# **15. How to generate a single random integer number using NumPy built-in function?**

# In[32]:


np.random.randint(1, 10, 5)


# In[ ]:





# **16. Write a code to generate a 7x5 matrix of 35 random numbers? use rand here** <br>
# *Notice, there are no ( ) in the output matrix!*

# In[34]:


np.random.rand(7,5)  


# In[35]:





# **17. Generate the following matrix using NumPy's built-in method for identity matrix.**

# In[36]:


x = 5.0 * np.eye(5)

print(x)


# In[30]:





# ### You must be feeling comfortable using NumPy now!
# # Great Job and Good Luck 
