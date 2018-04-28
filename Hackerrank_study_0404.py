
# coding: utf-8

# ### Coding Study_0404
# Hackerrank> algorithm> Implements (3문제)
# 
# - Cut the sticks : O.K
# - Non-Divisible Subset : X
# - Reapeated String : O.K


### Cut the sticks

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))


while(len(arr)):
    print(len(arr))
    arr = [x - min(arr) for x in arr if x - min(arr)>0]



### Non-Divisible Subset

nk = input().split()

n = int(nk[0])
k = int(nk[1])
S = list(map(int, input().rstrip().split()))

answer_i = []
answer_j = []

for i in range(n): 
    for j in range(n):
        if (S[i] + S[j]) % k ==0:

            answer_i.append(i)
            answer_j.append(j)

empty = []
for k in set(answer_i):
    l = answer_i.count(k)
    empty.append(l)
    
print(n - empty.count(max(empty)))



### Reapeated String

#!/bin/python3

import sys

def repeatedString(s, n):
    # Complete this function
    if len(s) >= n :
        return s[:n].count('a')
    
    else:
        if n % len(s) == 0:
            return s.count('a') * (n // len(s))
        else:
            return s.count('a') * (n // len(s)) + s[:(n%len(s))].count('a')

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)

