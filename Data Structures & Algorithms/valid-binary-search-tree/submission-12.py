# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check = True
        def dfs(root,left,right):
            nonlocal check
            if not root:
                return 
            if not (root.val > right and root.val < left):
                check = False
            dfs(root.left,root.val,right)
            dfs(root.right,left,root.val)
            return 0
        dfs(root,float("inf"),-float("inf"))
        return check
