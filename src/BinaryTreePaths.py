# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root==None:return []
        result=self.dfs(root)
        result=['->'.join(i) for i in result]
        return result
    def dfs(self,root):
        if root.left==None and root.right==None:return [[ str(root.val) ]]
        leftresult,rightresult=[],[]
        if root.left!=None:
            leftresult=self.dfs(root.left)
        if root.right!=None:
            rightresult=self.dfs(root.right)
        result=[]
        print leftresult
        for i in leftresult:
            result.append([str(root.val)]+i)
        for i in rightresult:
            result.append([str(root.val)]+i)
        return result


root=TreeNode(0)
node=TreeNode(1)
root.left=node
sol=Solution()
print sol.binaryTreePaths(root)