# coding=utf-8
__author__ = 'lenovo'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValid(self, root,leftval,rightval):
        if root==None:return True
        if not (leftval<root.val<rightval):return False
        if root.left!=None:
            if root.left.val>=root.val:
                return False
            flag=self.isValid(root.left,leftval,root.val)
            if flag==False:return False
        if root.right!=None:
            if root.val>=root.right.val:
                return False
            flag=self.isValid(root.right,root.val,rightval)
            if flag==False:return False
        return True
    def isValidBST(self,root):
        return self.isValid(root,-(1<<32),1<<32)
#[10,5,15,null,null,6,20]