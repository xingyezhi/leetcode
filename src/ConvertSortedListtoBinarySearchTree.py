__author__ = 'xingyezhi'
# encoding: utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        stack=[]
        nodestack=[]
        if len(nums)==1:return TreeNode(nums[0])
        elif len(nums)==0:return None
        half=(len(nums))/2
        node=TreeNode(nums[half])
        nodestack.append(node)
        stack.append((half+1,len(nums),True))
        stack.append((0,half,False))
        root=node
        while len(stack)!=0:
           # print stack
            self.printstack(nodestack)
            subnum=stack.pop()
            if subnum[1]==subnum[0]+1:
                node=TreeNode(nums[subnum[0]])
                if len(nodestack)!=0:
                    self.updateNode(nodestack[-1],node,subnum[2])
                    if subnum[2]:nodestack.pop()
                continue
            elif subnum[1]<=subnum[0]:
                if subnum[2]:nodestack.pop()
                continue
            half=(subnum[1]-subnum[0])/2+subnum[0]
            node=TreeNode(nums[half])
            if len(nodestack)!=0:
                self.updateNode(nodestack[-1],node,subnum[2])
                if subnum[2]:nodestack.pop()
            nodestack.append(node)
            stack.append((half+1,subnum[1],True))
            stack.append((subnum[0],half,False))

        return root
    def updateNode(self,node,subnode,flag):
        if not flag:
            node.left=subnode
        else:
            node.right=subnode
    def sortedListToBST(self, head):
        sortedArray=[]
        while(head!=None):
            sortedArray.append(head.val)
            head=head.next
        return self.sortedArrayToBST(sortedArray)