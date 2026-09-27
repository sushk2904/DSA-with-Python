from collections import deque

head = [1,2,2,1]

elements = deque()
maxm = 0
curr = head
while curr != None:
    elements.append(curr.val)
    curr = curr.next

while elements:
    front = elements.pop()
    back = elements.popleft()
    maxm = max(front+back, maxm)

print(maxm)