__author__ = 'lenovo'
# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        newNode=ListNode(0)
        newNode.next=head
        l1=newNode
        l=r=head
        counts=1
        while counts<n:
           r=r.next
           counts+=1
        while r.next!=None:
            r=r.next
            l1=l
            l=l.next
        l1.next=l.next
        return newNode.next

sol=Solution()
node=ListNode(1)
node2=ListNode(0)
print sol.removeNthFromEnd(node,1)