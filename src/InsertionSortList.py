__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        addhead=ListNode(0)
        addhead.next=head
        if head==None or head.next==None:return
        cur=head.next
        head.next=None
        t=head
        while cur!=None:
            front=addhead
            if cur.val>t.val:
                front=t
            while front.next!=None and cur.val>front.next.val:
                front=front.next
            t=cur.next
            front.next,cur.next=cur,front.next
            cur,t=t,cur
        return addhead.next

    def printList(self,head):
        while head!=None:
            print head.val,
            head=head.next
        print
sol=Solution()
head=ListNode(1)
cur=head
for i in range(2,10):
    t=ListNode(i)
    cur.next=t
    cur=t
sol.printList(head)
sol.insertionSortList(head)
sol.printList(head)