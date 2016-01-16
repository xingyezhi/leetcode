__author__ = 'xingyezhi'
# encoding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if root==None:return 0
        left=right=0
        if root.left!=None:
            left=self.minDepth(root.left)
        if root.right!=None:
            right=self.minDepth(root.right)
        if left==0 or right==0:return abs(left-right)+1
        else:return min(left,right)+1