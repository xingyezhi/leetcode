__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepth(self,root,level):
        l1=l2=level
        if root.left!=None:
            l1=self.deepth(root.left,level+1)
        if root.right!=None:
            l2=self.deepth(root.right,level+1)
        return max(l1,l2)
    def maxDepth(self, root):
        if root==None:return 0
        return self.deepth(root,1)