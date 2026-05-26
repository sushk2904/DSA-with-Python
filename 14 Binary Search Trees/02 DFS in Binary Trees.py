class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

one = Node(1)
two = Node(2)
three= Node(3)
four = Node(4)
five = Node(5)
six= Node(6)
seven= Node(7)
eight= Node(8)
nine = Node(9)
ten = Node(10)

three.left = two 
three.right = nine
eight.left = one 
eight.right = six
four.left = eight
four.right = ten
five.left = three
five.right = four

def preorder_traversal(node):
    if node ==  None:
        return 
    print(node.val, end = "")
    preorder_traversal(node.right)
    preorder_traversal(node.left)

preorder_traversal(five)

#TC = O(N) and SC = O(H)
