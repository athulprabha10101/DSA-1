def binary_search(my_list, target):
    start = 0
    end = len(my_list) - 1

    while (start <= end):
        mid = (start + end) // 2

        if target < my_list[mid]:
            end = mid - 1

        elif target > my_list[mid]:
            start = mid + 1

        else:
            return mid

    return -1


arr = [1, 2, 3, 4, 5,6, 7, 8, 9,10,89]
target = 10

index = binary_search(arr, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")