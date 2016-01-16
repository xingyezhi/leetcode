__author__ = 'lenovo'
# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1,l2):
        alist1=[]
        while l1!=None:
            alist1.append(l1.val)
            l1=l1.next
        alist2=[]
        while l2!=None:
            alist2.append(l2.val)
            l2=l2.next
        if len(alist1)<len(alist2):
            alist1.extend([0 for i in range(len(alist1),len(alist2))])
        elif len(alist1)>len(alist2):
            alist2.extend([0 for i in range(len(alist2),len(alist1))])
        c=0
        result=[]
        for i in range(len(alist1)):
           sum=alist1[i]+alist2[i]+c
           result.append(sum%10)
           c=sum/10
        if c!=0:
            result.append(c)
        tempNode=ListNode(result[-1])
        for i in range(len(result)-2,-1,-1):
            rnode=ListNode(result[i])
            rnode.next=tempNode
            tempNode=rnode
        return tempNode
l1=ListNode(0);
l2=ListNode(0);
solution =Solution()
print solution.addTwoNumbers(l1,l2)