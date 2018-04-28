
# coding: utf-8

# ### Algorithms - Warmup

# #### 6. Plus_Minus

# In[4]:


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

A = B = C = 0
for i in ar:
    if i > 0:
        A+=1

    elif i < 0:
        B+=1

    else:
        C+=1

print(A/n)
print(B/n)
print(C/n)


# #### 7. Staircase

# In[8]:


n = int(input().strip())
for i in range(1, n+1):
    print(" "*(n-i) + "#"*i)


# #### 8. Mini-Max Sum   <- 어떻게 풀엇는지 물어보기

# In[1]:


arr = list(map(int, input().strip().split(' ')))

max_sum, min_sum, sum_ttl, sum_other = 0, 0, 0, 0

for num in arr:
    sum_ttl += num
    
min_sum = sum_ttl

for i in range(len(arr)):
    sum_others = sum_ttl - arr[i]
    
    if sum_others < min_sum:
        min_sum = sum_others
        
    if sum_others > max_sum:
        max_sum = sum_others
        
print(min_sum, max_sum)


# In[23]:


import sys

arr = list(map(int, input().strip().split(' ')))
max=-sys.maxsize-1
min=sys.maxsize
sum=0
for x in arr:
    sum+=x
    if x>max:
        max=x
    if x<min:
        min=x
print (sum-max,sum-min)


# In[ ]:


### sort로 푸는것도 안됨.....ㅅㅂ


# #### 9. Birthday Cake Candles <- 왜 쥬피터에서는 안됨?

# In[37]:



import sys

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

print (arr.count(max(arr)))

        


# #### 10. Time Conversion <- 차이를 발생시키는 부분만 집중할 것 (시간부분, AM/PM부분)

# In[49]:


t = input()
AP = t[-2:]
if AP=="PM" and t[:2] != "12":
    t = str(12 + int(t[:2])) + t[2:] 
if AP == "AM" and t[:2] == "12":
    t = "00" + t[2:]
print(t[:-2])


# In[ ]:


## Offset을 한 값은 "string"-> "12"로 문자화 해줘야 한다.

