class Node:
    def __init__(self,val):
        self.val = val
        self.left =  None
        self.right = None

drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

drinks.left = hot
drinks.right = cold

hot.left = coffee
hot.right = tea

cold.left = cola
cold.right = fanta

print(drinks.val)
print(drinks.left) # this must have the same address as the hot
print(hot)
print(drinks.left.right.val)
print(drinks.left.left.val)
print(drinks.left.left.left.val) # will throw an attribute error because nonetype object has no val