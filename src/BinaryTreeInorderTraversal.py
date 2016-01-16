__author__ = 'xingyezhi'
# encoding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        stack,result=[],[]
        temp=root
        while temp!=None:
            stack.append(temp)
            temp=temp.left
        while len(stack)!=0:
            temp=stack.pop()
            result.append(temp.val)
            sub=temp.right
            while sub!=None:
                stack.append(sub)
                sub=sub.left
        return result
