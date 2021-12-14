
# First we make list which contatins assignment numbers
assign_numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# Question 1
print("\nThis is our first question")
for assign_number in assign_numbers:
    print(assign_number)

# Question 2
print("\nThis is our Second question")
for assign_number in assign_numbers:
    print(f"{assign_number}: {assign_number**2}")

# Question 3
print("\nThis is our Third question")
total = 0
for assign_number in assign_numbers:
    total += assign_number
print(total)

# Question 4
print("\nThis is our forth question")
total = 1
for assign_number in assign_numbers:
    total *= assign_number
print(total, "\n")