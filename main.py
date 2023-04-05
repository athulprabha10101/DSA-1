class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, " ", end="")
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True

    def pop(self):
        if self.head is None and self.tail is None:# edge case where ll is empty
            return None
        temp = self.head
        pre = self.head
        ''' we have to pop the last item. Pre = temp in the first iteration, and when temp.next is not none,
        pre will point at the second last node. Now, temp is at the last node which is to be popped.
        Since pre has the new last node after pop(), we can set tail = pre .This is  the only use of pre. Now, set
        tail.next = None'''
        while (temp.next is not None):
            '''The loop will stop when temp.next is None, and at that time, temp will point at the last node, ie
            the node to be popped, and pre will point to the new last node after pop()'''
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        '''another edge case is where there is only one node in the list, in that case, the while loop above does not run as temp.next is None, tail is already == pre and tail.next is already == None. list length is decremented to 0, but the problem is, tail and head and will still be pointing at the last node, so the list is still not empty. All we need to do is, check if after the length is 0  after decrement and then point self.head and self.tail to None.'''
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # returns the node that was popped


    def prepend(self,value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next # changes head to the next node
            temp.next = None # Removes node from the list
            self.length -=1
            if self.length == 0: # if the llist had onlt one value to begin with, and after execution of the
                self.tail = None # above code, head will be None since head.next and temp.next are None, and
                                 # tail is still pointing at the node. We need to change tail to None






ll1 = LList(33)
# print(ll1.head.value)
# print(ll1.tail.value)

ll1.append(333)
ll1.append(354)
ll1.append(55313)
ll1.append(8699)
ll1.print_list()
ll1.pop()
ll1.pop()
ll1.pop()
ll1.print_list()


