#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = input()
n_list = [i for i in n]
n_list = list(map(int, n_list))
print(sum(n_list))

