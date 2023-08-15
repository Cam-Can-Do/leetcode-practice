# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, low, high):
            if not root:
                return True
            left = isValid(root.left, low, root.val)
            right = isValid(root.right, root.val, high)
            return low < root.val < high and left and right

        return isValid(root, float("-inf"), float("inf"))
        
