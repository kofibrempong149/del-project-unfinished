#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas  as pd
import numpy as np
line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
import plotly.graph_objects as go
import plotly.express as px


# In[37]:


df = pd.read_csv("C:/Users/HP/Downloads/airline_data.csv")


# In[38]:


pd.set_option('display.max_columns',None)


# In[39]:


df.head()


# In[40]:


columns_to_select = ["Year", "Month", "Reporting_Airline", "OriginStateName", "DestCityName", "ArrDelay"]
df = df[df['Year'] == 2013][columns_to_select]


# In[41]:


df.head()


# In[42]:


line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()


# In[43]:


line_data


# In[48]:


import plotly.express as px

# Assuming 'line_data' is your DataFrame with 'Month' and 'ArrDelay' columns
fig = px.bar(line_data, x='Month', y='ArrDelay', title='Monthly ArrDelay') 
get_ipython().run_line_magic('matplotlib', 'inline')
fig.show()


# In[ ]:




