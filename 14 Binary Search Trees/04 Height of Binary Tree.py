#DFS Method
def height(node):
    if node == None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1


#BFS Method

from collections import deque

height = 0 
queue = deque([root])

while queue:
    level_len = len(queue)
    
    for _ in range(level_len):
        node = queue.popleft
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    height+=1

print(height)

