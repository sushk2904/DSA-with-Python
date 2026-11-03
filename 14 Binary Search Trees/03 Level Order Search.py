#I'm back at it again
from collections import deque
result = []
queue = deque([root])
while queue:
    level_len = len(queue)
    current_level = []
    for _ in range(level_len):
        node = queue.popleft()
        current_level.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    result.append(current_level)

print(result)
        