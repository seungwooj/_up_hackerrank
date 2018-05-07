
# coding: utf-8

# Coding Study_0329
# Hackerrank> algorithm> Implements (5문제)
# 
# - Find Digits : O.K
# - Extra Long Factorials : O.K
# - Append and Delete : O.K
# - Sherlock and Squares : O.K
# - Library Fine : O.K


# Find Digits

#!/bin/python3

import sys

def findDigits(n):
    # Complete this function
    
    answer = 0
    
    for i in list(str(n)):
        i = int(i)
        
        if i !=0 and n % i == 0:
            answer+=1
        else:
            answer=answer
            
    return answer
    
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)


# Extra Long Factorials

#!/bin/python3

import sys

def extraLongFactorials(n):
    # Complete this function
    
    answer = 1
    for i in range(2, n+1):
        answer *= i
    return answer

if __name__ == "__main__":
    n = int(input().strip())
    print(extraLongFactorials(n))


# Append and Delete

#!/bin/python3

import sys

def appendAndDelete(s, t, k):
    # Complete this function
    
    x = 0
    if len(s) > len(t):
        for n in range(len(list(t))):
            if list(s[:n+1]) == list(t[:n+1]):
                x += 1
    
    else:
        for n in range(len(list(s))):
            if list(s[:n+1]) == list(t[:n+1]):
                x += 1
            
    min_tr  = (len(s) - x) + (len(t) - x)    #최소로 필요한 횟수 구하기 (min_tr)

    if k > len(t) + len(s):
        return ("Yes")
    elif min_tr <= k and (k - min_tr) % 2 == 0:
        return ("Yes")
    else:
        return ("No")

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)


# Sherlock and Squares

#!/bin/python3

import sys

def squares(a, b):
    # Complete this function
    
    import math
    
    set = []
    for i in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b))+1):
        set.append(i)
    
    return len(set)

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)


# Library Fine

#!/bin/python3

import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Complete this function
    
    actual = y1 * 10000 +  m1 * 100 + d1
    due = y2 * 10000 + m2 * 100 + d2
    
    if due >= actual:
        return 0
    elif y1 != y2:                       #연도는 늦을 경우 무조건 큼 / 벌금 1순위
        return 10000 * (y1 - y2)
    elif m1 != m2:                       #연도가 늦은 케이스가 걸러질 경우 m1-m2 > 0일경우 무조건 벌금
        return 500 * (m1 - m2)
    else:                                #월과 마찬가지
        return 15 * (d1-d2)

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)

