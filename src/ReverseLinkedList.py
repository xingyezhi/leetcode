# coding=utf-8
__author__ = 'lenovo'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head==None:return None
        second,newhead=self.reverseList(head.next)
        if second!=None:
            second.next=head
            return head,newhead
        else:
            return head,head