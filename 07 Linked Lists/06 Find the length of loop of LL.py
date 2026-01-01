#Brute Force
head = [3,2,0,-4]
temp = head
my_dict = dict{}
travel = 0
while temp != None:
    if temp in my_dict:
        return travel -  my_dict[temp]
    
    my_dict[temp] = travel 
    travel +=1
    temp = temp.next

return None

#Optimized Soln

slow = head
fast = head
while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        slow = slow.next
        count = 1
        while slow != fast:
            slow = slow.next
            count+=1
        return count
            
