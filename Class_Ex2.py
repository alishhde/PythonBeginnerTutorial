""" Question:
    Write a program which is given an exam mark, and it returns a string — the grade for 
that mark — according to this scheme:
   Mark            Grade
   >=75            First
   [70, 75)     Upper Second
   [60, 70)        Second
   [50, 60)        Third
   [45, 50)       F1 Supp
   [40, 45)          F2
    < 40             F3
"""

# Answere 1
# grade = float(input("Enter your grade: "))
# if grade >= 75:             # grade >= 75
#     print("First")
# elif grade >= 70 and grade < 75:  # grade [70, 75)
#     print("Upper Second")
# elif grade >= 60 and grade <70: # grade [60, 70)
#     print("Second")
# elif grade >= 50 and grade <60: # grade [50, 60)
#     print("Third")
# elif grade >= 45 and grade <= 50: # grade [45, 50)
#     print("F1 Supp")
# elif grade >= 40 and grade < 45: # grade [40, 45)
#     print("F2")
# else:
#     print("F3")

# Answere 2
grade = float(input("Enter your grade: "))
if grade >= 75:              # grade >= 75
    print("First")
elif grade in range(70, 75):  # grade [70, 75)
    print("Upper Second")
elif grade in range(60, 70): # grade [60, 70)
    print("Second")
elif grade in range(50, 60): # grade [50, 60)
    print("Third")
elif grade in range(45, 50): # grade [45, 50)
    print("F1 Supp")
elif grade in range(40, 45): # grade [40, 45)
    print("F2")
else:
    print("F3")
