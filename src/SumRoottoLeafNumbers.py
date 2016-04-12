__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumTotal(self,node,nlist):
        nlist.append(node.val)
        if node.left==None and node.right==None:
            t=0
            for i in nlist:
                t*=10;t+=i
            self.total+=t
        if node.left!=None:
            self.sumTotal(node.left,nlist)
        if node.right!=None:
            self.sumTotal(node.right,nlist)
        nlist.pop()

    def sumNumbers(self, root):
        self.total=0
        if root!=None:
            self.sumTotal(root,[])
        return self.total

root=TreeNode(1)
left=TreeNode(2)
right=TreeNode(3)
root.left,root.right=left,right
sol=Solution()
print sol.sumNumbers(root)

