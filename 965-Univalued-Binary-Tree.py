# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        arr = set()
        def dfs(root):
            if not root:
                return
            arr.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return len(arr)==1
        