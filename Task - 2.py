#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv("01.Data Cleaning and Preprocessing.csv")


# In[3]:


dataset.info


# In[4]:


dataset.describe()


# In[5]:


dataset.shape


# In[6]:


dataset=dataset.drop_duplicates()


# In[7]:


dataset


# By removing the duplicates, the number of rows are reduced from 324 to 301

# In[8]:


dataset.isnull().sum()


# In[9]:


dataset.isnull().sum().sum()


# Total number of null values in dataset are 352

# Different ways of filling :

# In[10]:


dataset1= dataset.fillna(value=1)


# In[11]:


dataset1


# In[12]:


dataset1.isnull().sum().sum()


# In[13]:


dataset2= dataset.fillna(method='pad')


# In[14]:


dataset2


# In[15]:


dataset2.isnull().sum().sum()


# In[16]:


dataset3=dataset.fillna(method='bfill')


# In[17]:


dataset3


# In[18]:


dataset3.isnull().sum().sum()


# For summary statistics:
# Let us detect the outliers using IQR

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# In[20]:


dataset1.columns


# In[21]:


dataset1.drop(['Observation'],axis=1,inplace=True)
dataset1.columns


# In[22]:


Q1=dataset1.quantile(0.25)
Q3=dataset1.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[23]:


dataset1=dataset1[~((dataset1<(Q1-1.5*IQR))|(dataset1>(Q3+1.5*IQR))).any(axis=1)]


# In[24]:


dataset1


# In[ ]:




