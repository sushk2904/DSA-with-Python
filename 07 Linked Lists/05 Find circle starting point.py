#Brute force
head = [3,2,0,-4]
temp = head
my_set = set()
while temp!= None:
    if temp in my_set:
        return temp
    my_set.add(temp)
    temp = temp.next
    





#Optimized Soln
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    
    return None