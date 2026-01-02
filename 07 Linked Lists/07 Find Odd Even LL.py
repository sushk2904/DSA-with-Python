head = [8,0,1,4,5]
temp = head
values = []
while temp and temp.next:
    values.append(temp.val)
    temp = temp.next.next
if temp:
    values.append(temp.val)

temp = head.next
while temp and temp.next:
    values.append(temp.val)
    temp = temp.next.next
if temp:
    values.append(temp.val)

temp = head
index = 0
while temp is not None:
    temp.val = values[index]
    index +=1
    temp = temp.next
return head

#Optimized Soln
if head is None or head.next is None:
    return head
odd = head
even = head.next
even_head = eve
while even != None and even.next != None:
    odd.next = odd.next.next
    odd = odd.next
    even.next =  even.next.next
    even = even.next
odd.next = even_head
return head
