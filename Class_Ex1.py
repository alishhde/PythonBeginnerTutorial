""" Question: 
    Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
Write a program that asks a day number, and prints the day name (a string).
"""

# First we take the days number from the user
day_number = int(input("Please enter the day number: "))

# Now we want to compare the number to understand which day is it.
if day_number == 0:
    print("Sunday")
elif day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
else:
    print("Saturday")
