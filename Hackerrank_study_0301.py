
# coding: utf-8

# Coding Study_0301
# 
# Hackerrank> algorithm> Implements (5문제)
# - Climbing the Leaderboard (SOLVED - timeout)
# - The Hurdle Race (SOLVED)
# - Designer PDF Viewer (SOLVED)
# - Utopian Tree (SOLVED)
# - Angry Professor (SOLVED)
# + Forming a Magic Square
# 

# Climbing the Leaderboard

def climbingLeaderboard(scores, alice):
    # Complete this function
    alice_rank = []
    for i in alice :
        scores.append(i)
        new_scores = sorted(list(set(scores)))
        cur_rank = len(new_scores) - new_scores.index(i)
        
        alice_rank.append(cur_rank)
    
    return alice_rank

    

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))


n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))

alice_rank = []
for i in alice :
    scores.append(i)
    new_scores = sorted(list(set(scores)))
    cur_rank = len(new_scores) - new_scores.index(i)
        
    alice_rank.append(cur_rank)
    
print ("\n".join(map(str, alice_rank)))
    


# The Hurdle Race

import sys

def hurdleRace(k, height):
    # Complete this function
    if max(height) - k > 0 :
        result = max(height) - k
    else:
        result = 0

    return result

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)

# Designer PDF Viewer

h = list(map(int, input().strip().split(' ')))  #숫자 26개 리스트로 변경
word = list(input().strip())                    #알파벳들 리스트로 변경

alphabet = list("abcdefghijklmnopqrstuvwxyz")   #알파벳의 리스트 만듦
result = []

for i in range(len(word)):
    
    outcome = len(word) * h[alphabet.index(word[i])]  #폭(단어의길이) * 높이(단어속 알파벳들이 알파벳 체계에서 나오는 위치를 h안에서 숫자값으로 연결)
    result.append(outcome)
    
print(max(result))                                    #넓이의 최대값

# Utopian Tree

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    if n % 2 == 1 :
        print (int(2 * ((2**((n + 1) / 2)) - 1) / (2 - 1)))  #초항이 2, 2씩곱하는 등비수열의 합
    else :
        print (int((2**((n + 2) / 2) - 1) / (2 - 1)))   ##초항이 1, 2씩 곱하는 등비수열의 합


a = [-1, -1, 2, 3, -1]
a.count(>0)



# Angry Professor

import sys

def angryProfessor(k, a):
    # Complete this function
    good = 0
    for i in a :
        if i <= 0 :
            good += 1
    
    if good >= k :
        result = "NO"
    else :
        result = "YES"
    
    return result
    
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)

