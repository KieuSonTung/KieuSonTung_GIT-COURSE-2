import logging

# Task 1

print('Hello World')

# Task 2

def add_two_nums(a, b):
    return a + b

# Task 3

def cal_sum_list(list):
    if list.count(None) >= 1:
        print('List handles non-number')
    else:
        result = sum(list)
        return result


my_list = [None, 1, 2]
print(cal_sum_list(my_list))