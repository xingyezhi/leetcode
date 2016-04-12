__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        if root==None:return
        left=root.left
        right=root.right
        while left!=None:
            left.next=right
            left=left.right
            right=right.left
        self.connect(root.left)
        self.connect(root.right)