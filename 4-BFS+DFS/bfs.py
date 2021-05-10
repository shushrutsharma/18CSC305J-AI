# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, L, R):        
        if root == None:
            return 0
        res = 0
        q = [root]
        while q:
            next = []
            for node in q:
                if L <= node.val <= R:
                    res += node.val
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            q = next
            
        return res

bst = TreeNode(10, 7, 15)
Solution().rangeSumBST(bst,10,7,15)