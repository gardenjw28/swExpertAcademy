#!/usr/bin/env python
# coding: utf-8

# In[6]:


t = int(input())
add_list = list()
for tt in range(t):
    n = list(map(int, input().split()))
    add_list.append(i for i in n if i %2==1)
for x in range(len(add_list)):
    print("#{} {}".format(x+1, sum(add_list[x])))


# In[ ]:




