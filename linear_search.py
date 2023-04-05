# Given a list of integers and a target integer, find the first occurrence of the target integer in the list,
# or return -1 if it is not present. For example:

def linear_pos(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
        else:
            continue
    return -1

# Given a list of strings and a target string, find the index of the first occurrence of the target string in the list, or return -1 if it is not present. For example:

def linear_str(strarr, target):
    for i in strarr:
        if i == target:
            print("Number of",lintar,"is :",strarr.index(i))
            # return strarr.index(i)
            return True
    return False

lin = ["apple", "banana", "cherry", "date", "elderberry"]
lintar = "cherry"

f = linear_str(lin,lintar)
print(f)

# x = [1,3,4,5,1,2541,1251,3161,21,534]
# t = 3
#
# x = linear_pos(x,t)
# print("Index = ",x)
