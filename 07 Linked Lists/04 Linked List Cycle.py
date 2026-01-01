#Brute force
head = [3,2,0,-4]
temp = head
my_set = set()
while temp != None:
    my_set.add(temp)
    temp = temp.next
    if temp in my_set:
        print("true")
print("false")

#Optimized
slow = head
fast = head
while fast!=None and fast.next!=None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print("true")

print("false")

