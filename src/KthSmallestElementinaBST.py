# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        return self.kInorder(root,[k])
    def kInorder(self, root, k):
        if root==None:return None
        left=self.kInorder(root.left,k)
        if k[0]==0:return left
        k[0]-=1
        if k[0]==0:return root.value
        return self.kInorder(root,k)
