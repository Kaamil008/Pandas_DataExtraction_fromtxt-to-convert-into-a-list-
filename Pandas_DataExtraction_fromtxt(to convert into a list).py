#!/usr/bin/env python
# coding: utf-8

# # Importing pandas 

# In[27]:


import pandas as pd


# In[28]:


path =r'C:\Users\kaamil.kaleem\OneDrive - Vibracoustic\Desktop\Peak_Parameters.txt'


# In[29]:


f = open(path) 
f.read()


# # Converting the txt file into pandas dataframe(type of)

# In[34]:


df = pd.read_csv(path)
print(df)


# # Printing out the first row of the dataframe

# In[23]:


print(df.iloc[0])


# # Converting the df into a list 

# In[24]:


print(df.iloc[0].to_list())


# # extracting the first 3 values as list and storing it in another list

# In[25]:


x=[]
for i in range(len(df)):
    row_values = df.iloc[i].to_list()
    x.append(row_values[3:6])
print(x)


# In[26]:


y=[]
for i in range(len(df)):
    row_values = df.iloc[i].to_list()
    y.append(row_values[0:3])
print(y)


# In[ ]:




