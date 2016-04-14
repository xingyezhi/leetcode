# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def inorderTree(self,root,prenode):
    #     if root==None:return None
    #     l=self.inorderTree(root.left,prenode)
    #     l=prenode if l==None else l
    #     if self.firstget==False and l!=None and l.val>=root.val:
    #         self.first=l
    #         self.second=root
    #         self.firstget=True
    #     elif self.firstget==True and l.val>=root.val:
    #         self.second=root
    #     prenode=root
    #     r=self.inorderTree(root.right,prenode)
    #     return root if r==None else r
    def inorderTree(self,root,prenode):
        if root==None:return
        self.inorderTree(root.left,prenode)
        if self.firstget==False and prenode[0]!=None and prenode[0].val>=root.val:
            self.first=prenode[0]
            self.second=root
            self.firstget=True
        elif self.firstget==True and prenode[0].val>=root.val:
            self.second=root
            return
        prenode[0]=root
        self.inorderTree(root.right,prenode)
    def recoverTree(self, root):
        self.firstget=False
        node=None
        self.inorderTree(root,[node])
        self.first.val,self.second.val=self.second.val,self.first.val

#[0,1]
root=TreeNode(0)
left=TreeNode(1)
root.left=left
sol=Solution()
sol.recoverTree(root)

# def a(var1):
#     var1=TreeNode(1)
#
# t=5
# a(t)
# print t