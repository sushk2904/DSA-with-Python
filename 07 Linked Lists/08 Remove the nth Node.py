#Brute Force
temp = head
length = 0
while temp != None:
    length+=1
    temp = temp.next
    if length == n:
        urr_head = head.next
        del head
        return curr_head

index_of_element_removal = length - n
temp = head
count = 1

while count < index_of_element_removal:
    temp = temp.next
    count +=1

temp.next = temp.next.next
return head

#Optimized Soln
slow = head
fast = head
for i in range(0,n):
    fast = fast.next
if fast is None:
    return head.next
while fast.next is not None:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
return head
    