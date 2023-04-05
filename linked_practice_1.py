# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class Linked_List:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.value = new_node
#         self.tail = new_node
#         self.length = 1
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#
#     def get(self, index):
#         if index <= 0 or index > self.length:
#             return None
#         else:
#             temp = self.head
#             for _ in range(index):
#                 temp = temp.next
#         return temp.value
#
#     def set(self, index, value):
#         if index < 0 or index > self.length:
#             return None
#         else:
#             temp = self.head
#             for _ in range(index + 1):
#                 temp = temp.next
#         temp.value = value
#
#     def print_list(self):
#         temp = self.head
#         print()
#         while temp is not None:
#             print(temp.value," ",end = "")
#             temp = temp.next
#
#     def pop_last(self):
#         if self.length == 0:
#             return None
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         temp = self.head
#         pre = temp
#         while temp.next is not None:
#             pre = temp
#             temp = temp.next
#         pre.next = None
#         self.tail = pre
#         self.length -= 1
#
#     def pop_first(self):
#         if self.length == 1:
#             self.head = None
#             self.next = None
#         if self.length == 0:
#             return None
#         temp = self.head
#         self.head = temp.next
#         temp.next = None
#         self.length -= 1
#
#     def remove_by_index(self, index):
#         if index < 0 or index > self.length:
#             return None
#         if index == 0:
#             self.pop_first()
#         if index == self.length:
#             self.pop_last()
#         temp = self.head
#         pre = temp
#         for i in range(index + 1):
#             pre = temp
#             temp = temp.next
#         pre.next = temp.next
#         temp.next = None
#
#     def insert(self,value,index):
#         if index < 0 or index > self.length:
#             return None
#         else:
#             new_node = Node(value)
#             if index == 0:
#                 new_node.next = self.head
#                 self.head = new_node
#             else:
#                 temp = self.head
#                 pre = None
#                 for i in range(index):
#                     pre = temp
#                     temp = temp.next
#                 pre.next = new_node
#                 new_node.next = temp
#             self.length -=1
#
#
#     def delete_by_value(self, value):
#         temp = self.head
#         pre = None
#         while temp is not None:
#             if temp.value == value:
#                 if temp == self.head:
#                     self.head = self.head.next
#                 else:
#                     pre.next = temp.next
#                 if temp == self.tail:
#                     self.tail = pre
#                 self.length -= 1
#             else:
#                 pre = temp
#             temp = temp.next
#
#     def reverse(self):
#         # reverse tail head
#         temp = self.head
#         self.head = self.tail
#         # first define pre and post etc
#         pre = None
#         post = temp.next
#         # loop and change tmep.next to pre
#         for i in range(self.length):
#             post = temp.next
#             temp.next = pre
#             pre = temp
#             temp = post
#
#
#     # del by val - Pseudo
#     '''pre and next traverse, check if element is val(edge - head & tail), if val, connect prev to next, move to next'''
#     def delete_values(self, value):
#         pre = None
#         temp = self.head
#         while temp is not None:
#             if temp.value == value:
#                 if temp == self.head:
#                     self.head = temp.next
#                 else:
#                     pre.next = temp.next
#                     if temp == self.tail:
#                         self.tail = pre
#             else:
#                 pre = temp
#             temp = temp.next
#
#
#
#
#
#
# lin = Linked_List(900)
# lin.print_list()
# lin.append(300)
# lin.append(300)
# lin.append(300)
# lin.append(600)
# lin.append(500)
# lin.prepend(300)
# lin.append(300)
# lin.print_list()
# # lin.delete_by_value(300)
# lin.print_list()
# lin.reverse()
# lin.print_list()
# lin.insert(9000,1)
# lin.delete_values(300)
# lin.print_list()
#
# arr = [1,2,3,4,5]
# for i in arr:
#     lin

# lin methods

for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i,j,k)