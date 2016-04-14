# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if root==None:return []
        stack,result=[(root,False)],[]
        while len(stack)!=0:
            top=stack.pop()
            if top[1]:
                result.append(top[0].val)
                continue
            stack.append((top[0],True))
            if top[0].right!=None:
                stack.append((top[0].right,False))
            if top[0].left!=None:
                stack.append((top[0].left,False))
        return result

root=TreeNode(2)
r1=TreeNode(3)
r2=TreeNode(1)
root.right=r1
r1.right=r2
sol=Solution()
print sol.postorderTraversal(root)