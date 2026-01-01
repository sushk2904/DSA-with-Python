














#Tortoise-Hare Method
slow = head
fast = head
while fast!= None and fast.next!= None:
    slow = slow.next
    fast = fast.next.next

print("Middle of the linked list is:", slow)