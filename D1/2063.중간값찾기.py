#!/usr/bin/env python
# coding: utf-8

# In[8]:


n = int(input())

test_list = list(map(int, input().split()))
if len(test_list) == n:
    sort_list = sorted(test_list)
    mid = len(sort_list)//2+1
    print(sort_list[mid-1])


# In[ ]:




