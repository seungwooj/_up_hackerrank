
# coding: utf-8

#  Coding Study_0308
# Hackerrank> algorithm> Implements (6문제)
# 
# - Beautiful Days at the Movies : O.K
# - Viral Advertising : X
# - Save the Prisoner! : O.K
# - Circular Array Rotation : O.K
# - Sequence Equation : O.K
# - Jumping on th Clouds: Revisited : O.K


# Beautiful Days at the Movies

#!/bin/python3

import sys

def beautifulDays(i, j, k):
    # Complete this function
    count=0
    for num in range(i, j+1):
        if abs(num - int(str(num)[::-1])) % k == 0 :
               count +=1
    
    return count
        

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)

# Save the Prisoner!

#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    
    if s + m < n :
        answer = s + m - 1
        
    else:
        if (s + m - 1) % n == 0:
            answer = n
        else:
            answer = (s + m - 1) % n
            
    return answer

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

# Circular Array Rotation

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))

    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
        
a = a[n-(k%n):] + a[0:n-(k%n)]
    
for i in m:
    print (a[i])

# Sequence Equation  -> 설명할 수 있도록 준비

n = int(input().strip())
p = list(map(int, input().strip().split(' ')))
    
for i in range(n):
    print (p.index(p.index(i+1) + 1) + 1)

# Jumping on the Clouds: Revisited   <- 전제조건 : n % k = 0

n, k  = map(int, input().strip().split())
clouds = list(map(int, input().strip().split()))
    
print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))

