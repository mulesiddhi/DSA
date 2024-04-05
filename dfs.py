class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root):
        if root is None:
            return 
        visited = []
        stack = [root]
        while stack:
            node = stack.pop()
            visited.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        # print(visited)
        return visited
        
if __name__ == '__main__':
    # Construct a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Create an object of the class
    obj = Solution()
    print(obj.dfs(root))