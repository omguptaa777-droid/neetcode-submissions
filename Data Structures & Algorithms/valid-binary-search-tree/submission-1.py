# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.arr = []
        self.freq = {}
        self.flag = True
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if node.val in self.freq:
                self.flag = False
            self.freq[node.val] = 1 + self.freq.get(node.val,0)
            self.arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        if self.flag == False:
            return False
        return self.arr == sorted(self.arr)
