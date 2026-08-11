# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def DFS(root,maxNum):
            nonlocal count
            if not root:
                return
            count += 1 if root.val >= maxNum else 0
            maxNum = max(maxNum,root.val)
            DFS(root.left,maxNum)
            DFS(root.right,maxNum)
            return
        DFS(root,-float("inf"))
        return count
