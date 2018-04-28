
# coding: utf-8

# ### Algorithms - Implementation

# #### 1. Grading Students


n = int(input().strip())

grades = []
num_stu = 0

for num_stu in range(n):
    grades_in = int(input().strip())
    if grades_in >=38 :
        if grades_in % 5 >= 3:
            grades_out = (grades_in //5 + 1) * 5
        else : 
            grades_out = grades_in
        grades.append(grades_out)

    if grades_in < 38:
        grades_out = grades_in
        grades.append(grades_out)

result = grades
print ("\n".join(map(str, result)))


# #### 2. Apple and Orange
