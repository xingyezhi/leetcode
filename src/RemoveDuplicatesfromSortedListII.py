__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        result=addead=ListNode(0)
        temp=addead.next=head
        while temp!=None:
            value,flag=temp.val,False
            while temp.next!=None and temp.next.val==value:
                temp,flag=temp.next,True
            addead.next=temp;addead=temp
            temp=temp.next
        return result.next






