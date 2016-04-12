# coding=utf-8
__author__ = 'lenovo'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head==None or head.next==None:return None
        slower=fast=head
        while fast.next!=None and fast.next.next!=None:
            fast=fast.next.next
            slower=slower.next
            if fast==slower:
                front=head
                while front!=slower:
                    front=front.next
                    slower=slower.next
                return front
        return None
