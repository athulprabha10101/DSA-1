# Find the largest number in a given list

def largestnum(lis):
    largest = 0
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i] > lis[j]:
                if lis[i] > largest:
                    largest = lis[i]
    return largest

lis = [1222,190,21,34,54,56,90]
x= largestnum(lis)
print(x)

# using O(n)T

def largesum_n(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

lis = [1222,190,21000,34,5400,56,90]
x= largesum_n(lis)
print(x)

# find second largest O(n)T > WHat is the Space complexity ???

def secondlargest(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i

    second = 0
    for j in arr:
        if j != largest and j > second:
            second = j
    return second


'''alternatively
       if j == largest:
            continue
        if j > second:
            second = j'''

lis = [12222,190,21,34,54000,56,90]
x= secondlargest(lis)
print(x)