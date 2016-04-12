__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def isSameTree(self, p, q):
    #     if p==None and q==None:
    #         return True
    #     elif p!=None and q!=None:
    #         if p.val!=q.val:return False
    #         if not self.isSameTree(p.left,q.right):return False
    #         return self.isSameTree(p.right,q.left)
    #     else:
    #         return False
    # def isSymmetric(self, root):
    #     if root==None:return True
    #     return self.isSameTree(root.left,root.right)
    def isSymmetric(self, root):
        if root==None:return True
        p,q=root.left,root.right
        stackp,stackq=[p],[q]
        while len(stackp)!=0 and len(stackq)!=0:
            p,q=stackp.pop(),stackq.pop()
            if p==None and q==None:continue
            elif p==None or q==None:return False
            elif p.val!=q.val:return False
            stackp.append(p.left)
            stackq.append(q.right)
            stackp.append(p.right)
            stackq.append(q.left)
        return len(stackp)==len(stackq)