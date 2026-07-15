#We have to learn/remember or mug up somethings in it like queue data structure would be used.
from collections import deque
def level_order(node):
    result = []
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        e = queue.popleft() #O(1)
        result.append(e.val) #or e.data ALSO IT'S O(1)
        if e.left is not None:
            queue.append(e.left) #O(1)
        if e.right is not None:
            queue.append(e.right) #O(1)
    level_order(root)
    return result

"""Time complexity for this shii is TC-> O(N), SC -> O(N) + O(N)"""


