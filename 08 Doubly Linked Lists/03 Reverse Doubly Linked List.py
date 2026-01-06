def reverse_dll(self,val):
    head = [5,3,2,1,9]
    temp = self.head
    my_stack = []
    while temp is not None:
        my_stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        e = my_stack.pop()
        temp.val = e
        temp = temp.next
        