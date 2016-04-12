# coding=utf-8
__author__ = 'lenovo'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        result=[]
        from collections import deque
        queue=deque([root,None])
        pre=root
        while len(queue)>0:
            top=queue.popleft()
            if top==None:
                if pre==None:break
                else:
                    result.append(pre.val)
                    queue.append(None)
                    pre=top
                    continue
            pre=top
            if top.left!=None:queue.append(top.left)
            if top.right!=None:queue.append(top.right)
        return result

sol=Solution()
print sol.rightSideView(TreeNode(1))