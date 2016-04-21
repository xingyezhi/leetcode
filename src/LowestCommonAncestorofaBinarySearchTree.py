# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,node,cur,pathlist):
        if node==cur:return
        if node.val<cur.val:
            pathlist.append(1)
            self.dfs(node.right,cur,pathlist)
        else:
            pathlist.append(0)
            self.dfs(node.left,cur,pathlist)
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