__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        cur=root
        while cur!=None:
            if cur.left==None:break
            left=cur.left
            while left.right!=None:
                left=left.right
            left.right=cur
            cur=cur.left
        self.cur=cur

    def hasNext(self):
        return self.cur!=None


    def next(self):
        rs=self.cur.val
        cur=self.cur
        v=r=cur=cur.right
        while cur!=None:
            if cur.left==None:break
            left=cur.left
            while left.right!=None and left.right!=cur:
                left=left.right
            if left.right==cur:
                self.cur=v
                left.right=None
                break
            left.right=cur
            cur=cur.left
        self.cur=cur
        return rs

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())