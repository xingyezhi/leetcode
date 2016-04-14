# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        self.result,self.height=0,0
        leftmost=root
        while leftmost!=None:
            leftmost=leftmost.left
            self.height+=1
        if self.height>1:
            self.result+=2**(self.height-1)-1
        else:
            self.result=self.height
        self.recursion(root,1)
        return self.result
    def recursion(self,node,height):
        if node==None:
            return True
        if height==self.height-1:
            if node.left==None:
                return False
            elif node.right==None:
                self.result+=1
                return False
            else:
                self.result+=2
                return True
        return self.recursion(node.left,height+1) and self.recursion(node.right,height+1)

sol=Solution()
