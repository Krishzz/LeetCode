# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        # arr = []
        # queue = collections.deque([root])
        # while queue:
        #     level_data = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level_data.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     arr.append(level_data)
        # return arr
        arr = []
        def bfs(root, level, arr):
            if not root:
                return
            if len(arr)<level+1:
                arr.append([])
            arr[level].append(root.val)
            bfs(root.left, level+1,arr)
            bfs(root.right, level+1,arr)
        bfs(root, 0, arr)
        return arr

    # def bfss(self, root, level, arr):
    #     if not root:
    #         return
    #     if len(arr)<level+1:
    #         arr.append([])
    #     arr[level].append(root.val)
    #     self.bfs(root.left, level+1,arr)
    #     self.bfs(root.right, level+1,arr)

        
        