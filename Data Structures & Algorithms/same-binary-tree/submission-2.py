# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            for _ in range(len(q1)):
                Q1 = q1.popleft()
                Q2 = q2.popleft()
                if not Q1 and not Q2:
                    continue
                if not Q1 or not Q2 or Q1.val != Q2.val:
                    return False
                q1.append(Q1.left)
                q1.append(Q1.right)
                q2.append(Q2.left)
                q2.append(Q2.right)
        return True