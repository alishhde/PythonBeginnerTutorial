from os import system
from time import sleep

# str1 = input("Enter your TEXT: ")
str1 = "THIS IS SO FUN"

str1_len = len(str1)
counter = 0

while True:
    str1_lower = str1.lower()
    new_str = str1_lower[:counter]
    new_str += str1_lower[counter].upper()
    new_str += str1_lower[counter+1:]
    system('clear')
    print(new_str)
    sleep(0.7)

    if counter == (str1_len - 1):
        counter = 0
    else:    
        counter += 1
