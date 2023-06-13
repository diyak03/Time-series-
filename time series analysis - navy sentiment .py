#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_excel("RCN.xlsx")


# In[3]:


data


# lets look at the sentiment data: 
# - bar graph to check the distribution of the sentiment 
# - line graph to look at what the sentiment score looks like

# In[4]:


sen_counts = data['sentiment'].value_counts()

# Bar plot
plt.bar(sen_counts.index, sen_counts)

# Add labels and title
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Distribution')

# Display the plot
plt.show()


# In[5]:


plt.plot(data['sentiment_score'])

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Graph')

# Display the plot
plt.show()


# In[6]:


get_ipython().system('pip install --upgrade numpy')
get_ipython().system('pip install --upgrade pandas')


# In[7]:


grouped_data = data.groupby('tweetDate').sum()
grouped_data['sentiment_score']


# In[8]:


ss_data= pd.DataFrame(grouped_data['sentiment_score'])
ss = ss_data.reset_index()

print(ss)


# In[9]:


date_array = ss['tweetDate'].values
ss_array = ss['sentiment_score'].values


# In[10]:


plt.plot(date_array, ss_array)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment score over Time')

# Display the plot
plt.show()


# In[15]:


start_date = '2023-01-01'
end_date = '2023-04-01'

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

plt.plot(date_array, ss_array)

# Set the x-axis limits to the specified date range
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment score over Time')
plt.xlim(start_date, end_date)
plt.xticks(rotation='vertical')

# Show the plot
plt.show()


# In[ ]:




