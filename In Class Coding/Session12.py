# x = 1
# y = 3

# num = 1

# if num == 1:
#     summ = x + y
# elif num == 2:
#     summ = x * y
# elif num == 3:
#     summ == x/y
# else:
#     summ = x - y

# print(summ)

# d = {1:"Saturday", 2:"Sunday"}
# print(d.get(3))

day = "saturday"
num = 0

def day_of_the_week(dayy, number):
    list_of_the_days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for index in range(len(list_of_the_days)):
        if list_of_the_days[index] == dayy:
            day_index = index
            return day_index, list_of_the_days

    
ind, lst = day_of_the_week("Saturday", num)
num += ind
num %= 7
print(lst[num])