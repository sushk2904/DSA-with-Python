#Teacher Has told to do this on our own 
#You know the concept you can do this
#All you do is make head and tail
#then shift forward/backward the linking of the DLL 
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None



class StackDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        if self.tail is None:
            print("Stack Underflow")
            return None

        value = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return value

    def peek(self):
        if self.tail:
            return self.tail.data
        return None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")