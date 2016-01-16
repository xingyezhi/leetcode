__author__ = 'xingyezhi'
# encoding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
       def func(self,root):
            if root==None:return None
            if root.left==None and root.right==None:return root
            lefter=self.func(root.left)
            righter=self.func(root.right)
            if lefter!=None and righter!=None:
                root.right,lefter.right=root.left,root.right
                root.left=lefter.left=righter.left=righter.right=None
                return righter
            elif righter==None:
                root.right=root.left
                root.left=lefter.left=lefter.right=None
                return lefter
            elif lefter==None:
                righter.right=None
                return righter
       def flatten(self, root):
           self.func(root)

sol=Solution()
root=TreeNode(0)
root.left=TreeNode(1)
sol.flatten(root)
