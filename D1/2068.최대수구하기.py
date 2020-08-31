#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = int(input())

for n in range(t):
    test_list = list(map(int, input().split()))
    print("#{} {}".format(n+1, max(test_list)))


# In[ ]:




