# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,node,cur,pathlist):
        if node==cur:return True
        elif node==None:return False
        pathlist.append(1)
        if self.dfs(node.right,cur,pathlist):return True
        pathlist.pop()
        pathlist.append(0)
        if self.dfs(node.left,cur,pathlist):return True
        pathlist.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        pathp=[]
        self.dfs(root,p,pathp)
        pathq=[]
        self.dfs(root,q,pathq)
        for i in range(min(len(pathp),len(pathq))):
            if pathp[i]!=pathq[i]:
                break
            elif pathp[i]==0:
                root=root.left
            else:root=root.right
        return root