# def search_recursion(arr, target):
#     start = 0
#     end = len(arr)-1
#     return search_program(arr, target, start, end)
#
# def search_program(arr, target, start, end):
#     if start >= end:
#         return None
#     mid = (start+end)//2
#     if arr[mid] == target:
#         return mid
#     if target > arr[mid]:
#         return search_program(arr,target, mid+1, end)
#     else:
#         return search_program(arr, target, start, mid-1)
#
# arr = [1,2,3,4,5,6,7,8,9,10]
# print(search_recursion(arr, 3))



arr = [1,2,4,5,6,7,8]
start = 0
end = len(arr)-1

def binary_search_recursion(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    if target > arr[mid]:
        return binary_search_recursion(arr, target, mid+1, end)
    if target < arr[mid]:
        return binary_search_recursion(arr, target, start, mid-1)

print(binary_search_recursion(arr,4,start,end))


