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
