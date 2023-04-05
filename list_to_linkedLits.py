class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_lsit(self):
        if self.length == 0:
            print("Nothing to display")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, " ", end="")
                temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

arr = [1,2,3,4,5]
lis = LinkedList(arr[0])
for i in range(1, len(arr)):
    lis.append_node(arr[i])

lis.print_lsit()


