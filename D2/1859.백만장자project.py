#!/usr/bin/env python
# coding: utf-8

# In[26]:


t = int(input())
for tc in range(1,t+1):
    
    n = int(input())
    price_list = list(map(int,input().split()))
    buy_list = list()
    result = 0
    
    for i in range(n-1): #마지막 전까지만 
        if price_list[i] < max(price_list[i+1:]): # 이 값 뒤에 더 큰 값 있으니까 사기
            buy_list.append(price_list[i])

        else:
            result = (len(buy_list)*price_list[i] - sum(buy_list))
#             for x in buy_list:
#                 result += price_list[i] - x
            buy_list = list()

    for x in buy_list:
        result += price_list[len(price_list)-1] - x

    print("#{} {}".format(tc, result))


# In[ ]:





# In[5]:


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = list(map(int, input().split()))
    total = 0
    max_m = 0    
    for i in range(len(m)-1, -1, -1):

        if m[i] < max_m:
            total += max_m - m[i]

        else:
            max_m = m[i]

    print("#{} {}".format(tc, total))
    


# In[ ]:




