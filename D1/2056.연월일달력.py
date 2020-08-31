#!/usr/bin/env python
# coding: utf-8

# In[12]:


case = int(input())

for n in range(case):
    data = input()
    y, m, d = data[:4], data[4:6], data[6:]
    y, m, d = int(y), int(m), int(d)
    
    if  m == 2:
        if 1<= d and d <=28:
            print("#{} {:04}/{:02}/{:02}".format(n+1,y, m, d))
        else:
            print("#{} {}".format(n+1, -1))
    elif m in [1,3,5,7,8,10,12]:
        if 1 <= d and d <=31:
            print("#{} {:04}/{:02}/{:02}".format(n+1, y, m, d))
        else:
            print("#{} {}".format(n+1, -1))

    elif m in [4,6,9,11]:
        if 1 <= d and d <=30:
            print("#{} {:04}/{:02}/{:02}".format(n+1, y, m, d))
        else:
            print("#{} {}".format(n+1, -1))

    else:
        print("#{} {}".format(n+1, -1))


# In[16]:


case = int(input())

for n in range(case):
    data = input()
    y, m, d = data[:4], data[4:6], data[6:]
    y, m, d = int(y), int(m), int(d)
    
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if 1<= m <=12 and 1<= d <=day_list[m-1]:
        print("#{} {:04}/{:02}/{:02}".format(n+1, y, m, d))
    else:
        print(f"#{n+1} {-1}")


# In[ ]:




