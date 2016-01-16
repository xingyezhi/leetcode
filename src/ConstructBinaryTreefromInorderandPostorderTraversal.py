__author__ = 'xingyezhi'
# encoding: utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildNode(self, preorder,l1,r1,inorder,l2,r2):
        if r1==l1+1:
            return TreeNode(preorder[l1])
        elif r1<=l1:
            return None
        index=inorder.index(preorder[r1-1])
        root=TreeNode(preorder[r1-1])
        root.left=self.buildNode(preorder,l1,l1+index-l2,inorder,l2,index)
        root.right=self.buildNode(preorder,l1+index-l2,r1-1,inorder,index+1,r2)
        return root
    def buildTree(self, inorder, postorder):
        return self.buildNode(postorder,0,len(postorder),inorder,0,len(inorder))
sol=Solution()
sol.buildTree([1,2,3],[2,3,1])