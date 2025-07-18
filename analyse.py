#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[32]:


data = pd.read_csv(r"C:\Users\hicha\Documents\Python\Netflix Project\file.csv")


# # Getting some basic information about the dataset

# In[33]:


# show first 5 records
data.head(5)


# In[34]:


# show last 5 records
data.tail(5)


# In[35]:


# Overvieew about dataset
data.info()


# In[36]:


# shows number of columns and rows
data.shape


# In[37]:


# shows number of values in the dataset
data.size


# In[38]:


# shows all columnnames
data.columns


# In[39]:


# shows data types of each column
data.dtypes


# # Tasks

# # 1) is there any Duplicate record in the dataset ? If yes, then remove the duplicate records

# In[40]:


# Duplicate values are values that have been registered more than one time.
data.duplicated()


# In[42]:


# shows the duplicated rows
data[data.duplicated()]


# In[43]:


# shows duplicates completely
data[data.duplicated(keep = False)]


# In[47]:


# remove the duplicates rows permanently
data.drop_duplicates(inplace=True)


# In[48]:


# check if the duplicates have been removed
data[data.duplicated()]


# In[51]:


# Line 36: (7789,11)
data.shape


# # 2) Is there any NullValues presented in any column ? if yes, show with Heat-map

# In[54]:


# shows the NullValues
# True = Null-Values // False = no Null-Values
data.isnull()


# In[55]:


# shows null values in each column
data.isnull().sum()


# # Null-Values with Heat-map (Seaborn Library)

# In[74]:


import seaborn as sns


# In[82]:


sns.heatmap(data.isnull(), cmap="YlGnBu")


# In[ ]:




