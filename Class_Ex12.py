
def day(day_name="Monday", day_number=3):
    day_list = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    remainder = day_number % 7
    index_Counter = 0

    for i in day_list:
        if day_name == day_list[index_Counter]:
            break
        else:
            index_Counter += 1
    
    sum_index = remainder + index_Counter

    if sum_index > 6:
        sum_index -= 6

    return day_list[sum_index]

print(day())
    