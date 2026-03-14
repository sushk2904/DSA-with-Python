"""Dequeue class 
double ended queue, what it basically does is that it uses a doubly linked list
"""
from collections import deque

lst = deque([])

lst.append(100)
lst.append(120)
lst.append(150)
lst.appendleft(1)
lst.appendleft(9)

print(lst)
lst.pop()
print(lst)
lst.popleft()
print(lst)
