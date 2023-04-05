# find the sum of digits in a given number

def sum_of_nums(number):
    sum = 0
    while number:
        sum = sum + number%10
        try:
            number = number//10
        except:
            continue
    return sum
#
# '''Alternatively'''
#
def sum_of_nums_split(number):
    x = str(number)
    arr = []
    for i in x:
        arr.append(int(i))
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

num = int(input("Enter Number : "))
print(sum_of_nums(num))

print(sum_of_nums_split(3212))
