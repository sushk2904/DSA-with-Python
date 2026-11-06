from collections import deque



if not root:
    return []

result = []
queue = deque([root])
while queue:
    level_len = len(queue)
    for i in range(level_len):
        node = queue.popleft()
        
        if i == 0:
            result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
return result