# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        check = False
        def dfs(root):
            nonlocal check
            if not root:
                return 0
            if self.isSameTree(root,subRoot):
                check = True
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return check

        
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))