''' find the smallest number in a list and the second smallest'''

def smallest_num(list):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

def second_smallest(list):
    sm = smallest_num(list)
    second_smallest = list[0]
    for i in list:
        if i != sm and i < second_smallest:
            second_smallest = i
    return second_smallest

lis = [9,12,34,2,43,1,43,555]
print(second_smallest(lis))