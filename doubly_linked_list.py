class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            print("No values in list")
        temp = self.head
        while temp is not None:
            print(temp.value, " ", end="")
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:             #or if self.length == 0
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
        self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            return temp

    def get(self, index):
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1, index,-1):
                temp = temp.prev
            return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length +=1
        return True

    def remove(self,index):
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        if index < 0 or index > self.length:
            return False
        current = self.get(index)
        current.prev.next = current.next
        current
        current.next = None
        current.prev = None
        self.length-=1
        return current



newList = DoublyLinkedList(10)
newList.print_list()
newList.append(100)
print()
newList.print_list()
newList.pop()
print()
newList.print_list()
print()
newList.prepend(99)
newList.print_list()
newList.pop_first()
print()
newList.print_list()
newList.set_value(0,99)
print()
newList.print_list()
print()
newList.append(30)
newList.append(25)
newList.append(49)
newList.print_list()
newList.insert(2,1000)
print()
newList.print_list()
print()
newList.remove(2)
newList.print_list()