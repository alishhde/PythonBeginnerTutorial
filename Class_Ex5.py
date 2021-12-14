
# First we take the number from the input
number = int(input("Enter the number please: "))

counter = 0
for i in range(0, number, 2):
    print(i)
    # if i % 2 == 0:
    #     print(i)
    #     counter += 1
        
print(counter)