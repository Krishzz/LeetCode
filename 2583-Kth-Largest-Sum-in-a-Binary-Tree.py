# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        depth = 0
        def dfs(root, depth):
            if not root:
                return
            if len(arr)>depth:
                arr[depth]+=root.val
            else:
                arr.append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root, depth)
        print(arr)
        arr.sort(reverse=True)
        return arr[k-1] if len(arr)>=k else -1

        