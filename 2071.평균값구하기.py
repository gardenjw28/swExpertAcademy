#!/usr/bin/env python
# coding: utf-8

# In[2]:


t = int(input())
for n in range(t):
    test_list = list(map(int, input().split()))
    print("#{} {}".format(n+1, round(sum(test_list)/10)))


# In[ ]:




