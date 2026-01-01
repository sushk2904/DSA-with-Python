class Node:
    def __init__(self,val):
        self.val = val
        self.next =  None

node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 =  Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print("Node address:", node1)
print("Node value:", node1.val)
print("Node next address:", node1.next)
print("Node next value:", node1.next.val)
print("Node4 value", node1.next.next.next.val)