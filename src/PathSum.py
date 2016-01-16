__author__ = 'xingyezhi'
# encoding: utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root==None:return False
        elif root.val==sum and root.left==None and root.right==None:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
