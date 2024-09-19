# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        def dfs(root,level, arr):
            if not root:
                return 
            if len(arr)<level+1:
                arr.append([])
            arr[level].append(root.val)
            dfs(root.left, level+1, arr)
            dfs(root.right, level+1, arr)
        dfs(root,0, arr)
        return arr[::-1]