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

    def append_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_lsit(self):
        if self.length == 0:
            print("Nothing to display")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, " ", end="")
                temp = temp.next

    def pop_last(self):
        if self.head is None and self.tail is None:  # edge case where ll is empty
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def get_node_at_index(self, index):
        if index < 0 or index >= self.length:  # given index out of bounds, >= as init length is 1
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_node_at_index(index)
        if temp is not None:
            temp.value = value
            return True
        return print("Error")

    def insert_node(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_node(value)
        new_node = Node(value)

        temp = self.get_node_at_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove_item(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
            self.length =-1
        if index == self.length-1:
            return self.pop_last()
            self.length = -1
        pre = self.get_node_at_index(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -=1
        return temp

    def reverse(self):
        '''in order to reverse  the .next of every node to its previous, first reverse head and tail'''
        temp = self.head
        self.head = self.tail
        self.tail = temp
        '''add variables to left and right of temp'''
        after = temp.next
        before = None
        '''crawl thru '''
        for i in range(self.length):
            '''on every iteration, after becomes temp.next, temp.next reverses to before, before becomes temp, temp becomes after'''
            after = temp.next
            temp.next = before
            ''' after temp.next flips to before, there is no connection between temp and after'''
            before = temp
            ''' so before has to become next now and only then temp should become after, and in the next iteration, after moves to temp.next | 
            ie, after to next, temp is flipped, before is temp, temp is after'''
            temp = after

lis = LinkedList(1)
lis.print_lsit()
print("Print()")
print(lis.head.value)
print("Append()")
lis.append_node(2)
lis.print_lsit()
print("\nPrepend()")
lis.prepend(3)
lis.print_lsit()
lis.pop_last()
print("\nPop()")
lis.print_lsit()
print()
lis.prepend(3)
lis.print_lsit()
print()
lis.append_node(4)
lis.prepend(5)
print(lis.length)
print()
lis.print_lsit()
print("Get()")
print(lis.get_node_at_index(3).value)
print("Set()")
print(lis.set_value(3, 400))
lis.print_lsit()
print("\nInsert()")
lis.insert_node(0, 10000)
lis.insert_node(1, 3000)
lis.print_lsit()
print()
lis.remove_item(0)
lis.print_lsit()
print()
lis.reverse()
lis.print_lsit()



