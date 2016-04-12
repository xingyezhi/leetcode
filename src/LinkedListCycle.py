# coding=utf-8
__author__ = 'lenovo'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head==None:return False
        cur=head
        addhead=ListNode("addhead")
        while cur!=None:
            if cur.next==addhead:
                return True
            t=cur.next
            cur.next=addhead
            cur=t
        return False

node=ListNode(1)
sol=Solution()
print sol.hasCycle(node)