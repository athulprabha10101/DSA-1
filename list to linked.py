class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class L_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def print_nodes(self):
        #edge - list none
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

arr = [1,2,3,4,5,6]
link = L_list()
for i in arr:
    link.append(i)

link.print_nodes()


