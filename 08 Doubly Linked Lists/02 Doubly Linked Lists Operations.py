#How to create a node

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev =  None

"""if i do n1 = Node(10)
           n2 = Node(15)
           n3 = Nonde(8)
This will create 3 different nodes and if we want to interconnect this:-
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
"""

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #1. Insert at Head
    def  insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
    
    #2 Append at last
    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current:
                current = current.next  #Doubt?
            current.next = new_node
            new_node.prev = current
    
    #3 Insert in between
    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return
    
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count+=1
        
        if current is None:
            print("print out of bounds")
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node


        #HW 
        '''create for traverse(), delete_head(), delete_last(), delete_in_between()'''


