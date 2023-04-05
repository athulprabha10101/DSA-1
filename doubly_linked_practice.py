class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value," ",end = "")
            temp = temp.next
        print()

    def append(self,value):
        new_node = Node(value)
        #edge - empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        #tail.next -> new and new.prev -> tail, tail is new
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop_last(self):
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

    def prepend(self,value):
        #edges - list is 0
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1

    def pop_first(self):
        #head = head.next. orig,next = none, edge - 1 node / 0 nodes
        if self.head == None:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -=1

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.value
        else:
            temp = self.tail
            for i in range(self.length-1,index,-1):
                temp = temp.prev
            return temp.value

    def set(self,index,value):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.next.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        else:
            new_node = Node(value)
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                if index == 0:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                elif index == self.length:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                else:
                    temp = self.head
                    for i in range(index):
                        temp = temp.next
                    before = temp.prev
                    before.next = new_node
                    new_node.prev = before
                    new_node.next = temp
                    temp.prev = new_node
            self.length +=1

    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        else:
            if self.length == 0:
                return None
            elif self.length == 1:
                self.head = None
                self.tail = None
            elif index == 0:
                temp = self.head
                self.head.prev = None
                self.head = self.head.next
                temp.next = None
                self.head.prev = None
            elif index == self.length:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
            else:
                temp = self.head
                pre = None
                for i in range(index):
                    pre = temp
                    temp = temp.next
                pre.next = temp.next
                temp.next.prev = pre
                temp.next = None
                temp.prev = None
            self.length-=1







doubly = Doubly(13)
doubly.print()
doubly.append(33)
doubly.print()
doubly.pop_first()
doubly.print()
doubly.append(434)
doubly.append(653)
doubly.append(12133)
doubly.print()
print(doubly.get(3))

