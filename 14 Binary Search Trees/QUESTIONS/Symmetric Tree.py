def isSymmetric(self, root: TreeNode | None) -> bool:
    if not root:
        return True

    queue = deque([root])
    while queue:
        level_len = len(queue)
        current_level = []
        for _ in range(level_len):
            node = queue.popleft()
            if node:
                current_level.append(node)
                queue.append(node.left)
                queue.append(node.right)
            else:
                queue.append(None)
        
        back_pointer = len(current_level)
        for i in range(len(current_level)//2):
            if current_level[i] != current_level[back_pointer-1]:
                return False 
            back_pointer -=1
        
        return True


