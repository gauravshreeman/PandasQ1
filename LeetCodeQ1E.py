#!/usr/bin/env python
# coding: utf-8

# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
# 
# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
# 
# The result format is in the following example.

# In[2]:


#code 
import pandas as pd

student_data = { 'student_id' : ['210', '211', '212', '213'],
                'age' : ['13', '17', '14', '15']}
dataframe = pd.DataFrame(student_data)
print (dataframe)


# In[ ]:




