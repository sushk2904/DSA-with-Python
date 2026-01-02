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
    