class Solution:
    def maxDepth(self, root):
        
        # Base case
        if root is None:
            return 0

        # Find left subtree height
        left = self.maxDepth(root.left)

        # Find right subtree height
        right = self.maxDepth(root.right)

        # Return maximum height
        return max(left, right) 