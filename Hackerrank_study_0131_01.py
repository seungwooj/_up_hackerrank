
# coding: utf-8

# ### Algorithms - Warmup

# #### 1. Solve Me First

# In[1]:


def solveMeFirst(a,b):
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


# #### 2. Simple Array Sum

# In[10]:


import sys

def simpleArraySum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)


# In[13]:


number_of_elements = int(input())
array = map(int, input().split())
print (sum(array))


# #### 3. Compare the Triplets

# tripletA = (a0,a1,a2), tripletB = (b0,b1,b2)
# ai > bi : Alice earn 1 point
# ai < bi : Bob earn 1 point
# ai = bi : No points 
# 
# Input Format
# 
# The first line contains  space-separated integers, a0, a1, and a3, describing the respective values in triplet . 
# The second line contains  space-separated integers, b0, b1, and b3, describing the respective values in triplet .
# 
# Constraints
# a , b 둘다 1이상 100이하
# 
# Output Format
# 
# Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.
# 
# 

# In[49]:


import sys

def solve(a, b):
    A = B = 0
    for i in range(3):
        if a[i] > b[i]:
            A += 1
        elif a[i] < b[i]:
            B += 1
        else:
            A += 0
            B += 0
    result = [A, B]
    return result

a0, a1, a2 = input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]
result = solve(a, b)
print (" ".join(map(str, result)))


# #### 4. A Very Big Sum

# In[46]:


n = int(input().strip())
ar = list(map(int, input().strip().split(" ")))
print(sum(ar))


# #### 5. Diagonal Difference   : a_t 자체가 a 를 행렬로 출력해주는 식임. -> a[i][i] 입력 가능함

# In[3]:


import sys

def diagonalDifference(a):
    # Complete this function
    
    diag_left = 0
    diag_right = 0
    
    for i in range(len(a)):
        j = (len(a)-1)-i
        diag_left += a[i][i]
        diag_right += a[i][j]
        
    return abs(diag_left - diag_right)


if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)

