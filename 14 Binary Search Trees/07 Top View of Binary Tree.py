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
            node, line = q.popleft()

            # Store node only first time
            if line not in top_nodes:
                top_nodes[line] = node.val

            # Left child
            if node.left:
                q.append((node.left, line - 1))

            # Right child
            if node.right:
                q.append((node.right, line + 1))

        # Sort by horizontal distance
        result = []

        for key in sorted(top_nodes):
            result.append(top_nodes[key])

        print(result)