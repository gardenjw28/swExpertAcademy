#!/usr/bin/env python
# coding: utf-8

# In[1]:


A, B = input().split()
A, B = int(A), int(B)
d = {1:3, 2:1, 3:2}
if d[A] == B:
    print("A")
elif d[B] == A:
    print("B")


# In[2]:


a, b = map(int, input().split())
if (a,b) in [(2,1),(3,2),(1,3)]:
    print("A")
else:
    print("B")


# In[ ]:




