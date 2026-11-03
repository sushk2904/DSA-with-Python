def diameterofBinaryTree(self, root: Optional[TreeNode]) -> int: 
    self.diameter = 0
    def solve(root):
        if not root:
            print("0")
        
        left_height = solve(root.left)
        right_height = solve(root.right)

        self.diameter = max(self.diameter, left_height+ right_height)

        return 1 + max(left_height, right_height)

    solve(root)
    return self.diameter
