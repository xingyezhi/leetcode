__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rootPath(self,root):
        if root==None:return 0
        if type(root.val)==list:
            return root.val[1]
        left=self.rootPath(root.left)
        right=self.rootPath(root.right)
        root.val=[root.val,max(left,right,0)+root.val]
        return root.val[1]
    def maxPathSum(self, root):
        if root==None:return None
        left=self.maxPathSum(root.left)
        right=self.maxPathSum(root.right)
        self.rootPath(root)
        l=self.rootPath(root.left)
        r=self.rootPath(root.right)
        mid=root.val[0]
        if l>0:mid+=l
        if r>0:mid+=r
        return max(left,right,mid)

node1=TreeNode(2)
node2=TreeNode(-1)
node1.left=node2
sol=Solution()
print sol.maxPathSum(node1)