
'''2 --> Factorial of a given number'''

def factorial(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f

''' aletrnatively - using recursion '''

def factorail_recur(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

x = factorial(4)
print("without recursion",x)

x = factorail_recur(4)
print(x)
