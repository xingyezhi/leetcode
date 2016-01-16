__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        from collections import deque
        queue=deque([])
        result,temp=[],[]
        if root==None:return result
        queue.append(root)
        queue.append('#')
        while len(queue)!=1:
            top=queue.popleft()
            if top!='#':
                temp.append(top.val)
                if top.left!=None:queue.append(top.left)
                if top.right!=None:queue.append(top.right)
            else:
                result.append(temp)
                temp=[]
                queue.append('#')
        result.append(temp)
        return result[::-1]
