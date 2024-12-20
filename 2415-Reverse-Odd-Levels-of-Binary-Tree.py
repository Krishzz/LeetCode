# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth_first_search(left, right, level):
            if not left or not right:
                return
            if level%2 == 0:
                left.val, right.val = right.val, left.val
            depth_first_search(left.left, right.right, level+1)
            depth_first_search(left.right, right.left, level+1)
        depth_first_search(root.left, root.right, 0)
        return root