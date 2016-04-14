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
        while root!=None:
            cur,root=root,None
            while cur!=None:
                if cur.left!=None and cur.right!=None:
                    cur.left.next=cur.right
                    root=cur.left
                    pre=cur.right
                    cur=cur.next
                    break
                elif cur.left!=None or cur.right!=None:
                    pre=cur.left if cur.left!=None else cur.right
                    root=pre
                    cur=cur.next
                    break
                else:
                    cur=cur.next
            while cur!=None:
                if cur.left!=None:
                    pre.next=cur.left
                    pre=cur.left
                if cur.right!=None:
                    pre.next=cur.right
                    pre=cur.right
                cur=cur.next



sol=Solution()
one=TreeLinkNode(0)
sol.connect(one)
