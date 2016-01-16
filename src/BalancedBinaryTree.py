__author__ = 'xingyezhi'
# encoding: utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isBalanced(self, root):
        if root==None:return True
        else:return self.Visit(root)[1]
    def Visit(self,root):
        lheight=rheight=0
        if root.left!=None:
            lheight,isbalance=self.Visit(root.left)
            if not isbalance:return lheight,False
        if root.right!=None:
            rheight,isbalance=self.Visit(root.right)
            if not isbalance:return rheight,False
        if abs(lheight-rheight)<=1:
            return max(lheight,rheight)+1,True
        else:
            return 0,False