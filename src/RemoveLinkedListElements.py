# coding=utf-8
__author__ = 'lenovo'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        addhead=ListNode(-1)
        addhead.next=head
        pre,cur=addhead,head
        while cur!=None:
            if cur.val!=val:
                cur=cur.next
                pre=pre.next
            else:
                while cur!=None and cur.val==val:
                    cur=cur.next
                pre.next=cur
                if cur!=None:
                    pre,cur=cur,cur.next
        return addhead.next