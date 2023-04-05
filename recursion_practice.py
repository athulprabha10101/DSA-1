# def recur_print(n):
#     print(n)
#     recur_print1(1)
#
# def recur_print1(n):
#     print(n)
#     recur_print2(2)
#
# def recur_print2(n):
#     print(n)
#     recur_print3(3)
#
# def recur_print3(n):
#     print(n)
#
# recur_print1(100)
#
#
# def rec_print(n):
#     if n == 5:
#         print(n)
#         return
#     print(n)
#     rec_print(n+1)
#
# rec_print(1)
#

# function to print x to x + 5

def xprint(n):
    if n < 1: # Base condition
        return
    print(n) # Action
    xprint(n-1) # Recursive case


xprint(10)