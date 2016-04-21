# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        if root==None:return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)