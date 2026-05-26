from collections import deque
def level_order(node):
    result = []
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        e = queue.popleft()
        result.append(e.data)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:

