__author__ = 'xingyezhi'
# encoding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        elif p!=None and q!=None:
            if p.val!=q.val:return False
            if not self.isSameTree(p.left,q.left):return False
            return self.isSameTree(p.right,q.right)
        else:
            return False