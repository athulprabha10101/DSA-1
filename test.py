# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#
# class Linked_list:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def reverse(self):
#         #traverse , temp.next = pre, edge - head,
#         pre = None
#         temp = self.head
#         self.head, self.tail = self.tail, self.head
#         while temp.next is not None:
#             next = temp.next
#             temp.next = pre
#             temp = next
#             pre = temp


    # def reverse_recursion(self):
    #     temp = self.head
    #     pre = None
    #     self.head, self.tail = self.tail,self.head
    #
    #
    #
    #     return

    # Factorial using recursion

def factorial(self,number):
    if number <= 1:

        return 1
    return number * factorial(number-1)

num = 5
print(factorial(num))



