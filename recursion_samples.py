def numbers_upto(x):
    if x == 0:
        return 0
    else:
        numbers_upto(x-1)
        print(x-1)

numbers_upto(10)


def factorial(n):
    print(n)
    if n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial :",factorial(4))



