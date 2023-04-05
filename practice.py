# Write a Python program to find the sum of all even numbers from 1 to n, where n is a user input.

# def add_evens(n):
#     sum = 0
#     for i in range(n):
#         if i % 2 == 0:
#            sum = sum+i
#     return sum
#
# print(add_evens(5))

# Write a Python function that takes a list of integers as input and returns the largest number in the list.



# def largest_of_list():
#     n = int(input("Enter list limit: "))
#     lis = []
#     for i in range(n):
#         val = int(input("Enter list values: "))
#         lis.append(val)
#
#     largest = 0
#     for i in range(n):
#         if lis[i] > largest:
#             largest = lis[i]
#     return largest
#
# x = largest_of_list()
# print(x)

# Write a Python program to reverse a given string. For example, if the input string is "hello", the output should be "olleh".

# def str_reverse(in_str):
#     s_len = len(in_str)
#     revstr = ""
#     for i in range(s_len-1,-1,-1):
#         revstr += in_str[i]
#     return revstr

# Method 2
# def str_reverse(in_str):
#     revstr = ""
#     for i in reversed(in_str):
#         revstr +=i
#     return revstr
#
#
# print(str_reverse("holiday"))

# Write a Python function that takes two strings as input and checks if they are anagrams. Anagrams are words that have the same letters but in a different order. For example, "listen" and "silent" are anagrams.

# def anagram(str_1, str_2):
#     s1count = 0
#     s2count =  0
#     for i in str_1:
#         if i not in str_2:
#             return False
#         else:
#             for i in str_2:
#                 if i not in str_1:
#                     return False
#             if str_1.count(i) == str_2.count(i):
#                 return True
#             else:
#                 return False
#
# print(anagram("anagram","angamary"))

# Write a Python program to find the factorial of a given number. The factorial of n is the product of all positive integers from 1 to n. For example, the factorial of 4 is 4 x 3 x 2 x 1 = 24.

# def factorial(n):
#     fa = 1
#     for i in range(1, n+1):
#         fa = fa*i
#     print(f"Factorial of {n} = ",fa)
#
# factorial(4)

# Write a Python function that takes a list of integers as input and returns a new list with only the even numbers from the original list.

# def even_list(my_list):
#     list2 = [i for i in my_list if i%2==0]
#     return list2
#
# '''alternatively'''
#
# def even_list(my_list):
#     evenarr = []
#     for i in my_list:
#         if i%2 == 0:
#             evenarr.append(i)
#     return evenarr
#
#
# l1 = [1,2,2,2,3,3,3,3,3,5,4,6,5]
# l2 = even_list(l1)
# print(l2)

# paindrome

# def palindrome(str1):
#     n = len(str1)
#     for i in range(n//2):
#         if str1[i] != str1[n-1-i]:
#             return False
#     return True
#
# x = palindrome("malayalamanorama")
# print(x)

# Write a Python function that takes a list of strings as input and returns a new list with only the strings that contain the letter "a".

# def list_with_a(mylist):
#     newlist = [str_a for str_a in mylist if "a" in str_a]
#     return newlist
#
#
# a = ["apple", "banana", "orange", "sox" , "shoe" , "rod"]
# b = list_with_a(a)
# print(b)

# Write a Python program to find the second largest number in a given list of integers.

# def second_largest(num_lsit):
#     largest = 0
#     second_largest = 0
#     for i in num_lsit:
#         if i > largest:
#             second_largest = largest
#             largest = i
#         elif i > second_largest:
#             second_largest = i
#     return second_largest
#
#
#
# arr = [9,4,2,2,3]
# print(second_largest(arr))

# Write a Python function that takes a list of integers as input and returns the sum of all the numbers in the list that are divisible by 3 or 5.

# def sum_list_3n5(my_list):
#     arr_3n5 = [x for x in my_list if x%3 == 0 or x%5 == 0]
#     sumof = 0
#     for i in arr_3n5:
#         sumof = sumof + i
#     print(sumof)
#
# my = [9,33,52,4,45,76,534,98,56,9,34,12,34,65,45,999,995]
# sum_list_3n5(my)

# Write a Python program that takes a string as input and returns the number of vowels in the string.

# def vowels_in_string(my_Str):
#     vowel_count = 0
#     for i in my_Str:
#         if i in "a" or i in "e" or i in "i" or i in "o" or i in "u":
#             vowel_count +=1
#     return vowel_count
#
# print(vowels_in_string("ooooooooooiiiii"))

# Write a Python function that takes two lists as input and returns a new list that contains only the common elements between the two lists.

# def commons_in_array(ar1, ar2):
    #method 1
    # arr3 = []
    # arr3 = set([i for i in ar1 for j in ar2 if i == j and i not in arr3])
    # return arr3
    # #method 2
    # ar3 = []
    # for i in ar1:
    #     for j in ar2:
    #         if i == j and i not in ar3:
    #             ar3.append(i)
    # return ar3
    # #method 3
    # arx = set(ar1).intersection(set(ar2))
    # return arx

# a = [1,2,3,4,5,24,13,4234,0]
# b = [0,0,2,1,24,24]
#
# y = (commons_in_array(a,b))
# print(y)

