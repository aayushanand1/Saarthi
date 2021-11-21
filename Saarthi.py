#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 6

dict_1={'hello':1, 'bye':2, 'no':3, 'hello':4}
test_dict=[]

result= dict()

for key,val in dict_1.items():
    if val not in test_dict:
        test_dict.append(val)
        result[key]= val


print(result)


# In[ ]:




