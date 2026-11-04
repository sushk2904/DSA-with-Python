from collections import deque
ans = []
result ={}
queue = deque()
queue.append((root, 0))
while len(queue)!=0:
    e, line = queue.popleft()
    result[line] = e.data
    if e.left:
        queue.append((e.left, line-1))
    if e.right:
        queue.append((e.right, line+1))

for value in sorted(result.items()):
    ans.append(value[1])

print(ans)
