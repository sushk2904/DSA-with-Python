from collections import deque

class Solution:
    def topView(self, root):
        
        # If tree is empty
        if not root:
            return []

        # Dictionary to store first node at each horizontal distance
        top_nodes = {}

        # Queue -> (node, horizontal distance)
        q = deque([(root, 0)])

        while q:
            node, hd = q.popleft()

            # Store node only first time
            if hd not in top_nodes:
                top_nodes[hd] = node.val

            # Left child
            if node.left:
                q.append((node.left, hd - 1))

            # Right child
            if node.right:
                q.append((node.right, hd + 1))

        # Sort by horizontal distance
        result = []

        for key in sorted(top_nodes):
            result.append(top_nodes[key])

        return result