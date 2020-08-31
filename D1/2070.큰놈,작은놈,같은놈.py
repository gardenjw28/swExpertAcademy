#!/usr/bin/env python
# coding: utf-8

# In[1]:


t= int(input())

for n in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    
    if a > b :
        print("#{} {}".format(n+1, ">"))
    elif a == b :
        print("#{} {}".format(n+1, "="))
    elif a < b :
        print("#{} {}".format(n+1, "<"))
        


# In[ ]:




