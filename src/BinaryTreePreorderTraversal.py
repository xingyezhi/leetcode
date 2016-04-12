# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        stack,result=[],[]
        while root!=None:
            stack.append(root)
            result.append(root.val)
            root=root.left
        while len(stack)!=0:
            top=stack.pop()
            rson=top.right
            while rson!=None:
                result.append(rson.val)
                stack.append(rson)
                rson=rson.left
        return result

root=TreeNode(2)
r1=TreeNode(3)
r2=TreeNode(1)
root.right=r1
r1.right=r2
sol=Solution()
print sol.preorderTraversal(root)

