__author__ = 'xingyezhi'
# encoding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,sum,stack):
        if root==None:return
        stack.append(root.val)
        if root.val==sum and root.left==None and root.right==None:
            self.result.append(stack[:])
            stack.pop()
            return
        self.dfs(root.left,sum-root.val,stack)
        self.dfs(root.right,sum-root.val,stack)
        stack.pop()
    def pathSum(self, root, sum):
        self.result=[]
        self.dfs(root,sum,[])
        return self.result

t=[1,2,3,4]
print t.extend([])
print t