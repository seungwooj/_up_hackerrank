
# coding: utf-8

# ### Coding Study_0221
# 
# Hackerrank> algorithm> Implements (7문제)
# - Sock Merchant
# - Drawing Book
# - Counting Valleys
# - Electronics Shop
# - Cats and a Mouse
# - Forming a Magic Square
# - Picking Numbers

# In[1]:


### Sock Merchant

def sockMerchant(n, ar):
    result = 0
    target = list(set(ar))
    for i in target:
        result = result + (ar.count(i)//2)
    
    return result



n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)


# In[2]:


### Drawing books

def solve(n, p):
    
    if p <= n // 2:
        answer = p // 2
    else :
        if n % 2 == 0 :
            answer = (n - p + 1) // 2
        else :
            answer = (n - p) // 2

    return answer
    # Complete this function

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)


# In[3]:



n = int(input().strip())
s = input().strip()

h = 0
change = []
for i in range(n):
    if s[i] == "U" :
        h +=1
    else : 
        h -=1

    change.append(h)
print(change)


# In[4]:


### Counting Valleys

def countingValleys(n, s):
    h = 0
    change = []
    for i in range(n):
        if s[i] == "U" :
            h +=1
        else : 
            h -=1

        change.append(h)
    
    result = 0
    for j in range(n-1):
        if change[j] == 0 and change[j+1] < 0:
            result += 1
    
    return result
        


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)


# In[4]:


### Electronics Shop

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

list_1 = []
for i in keyboards :
    
    for j in drives :
        sum = i + j
        list_1.append(sum)
    
list_2 = []
for k in list_1 :
    if s - k >=0:
        list_2.append(k)

    else : 
        list_2.append(-1)

print(max(list_2))


# In[1]:


### Cats and a Mouse

q = int(input().strip())
for a0 in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    
    if abs(x-z) > abs(y-z) :
        print ("Cat B")
    elif abs(x-z) < abs(y-z) :
        print ("Cat A")
    else:
        print("Mouse C")


# In[ ]:


### Forming a Magic Square  <- 실패

s = []
for s_i in range(3):
    s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
    s.append(s_t)

mat = np.array(s)
prop_sum = round((mat.sum() * 3 + mat[1,1]) / 8)

for i in range(3):
    for j in range(3):
        print 


# In[18]:


### Picking Numbers
import sys

def pickingNumbers(a):
    a.sort()
    list = []
    for i in range(n) :
        for j in range(n) :
            if abs(a[i] - a[j]) <=1:
                list.append(abs(i-j))
    result = max(list)+1
    return result

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)

