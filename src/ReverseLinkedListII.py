__author__ = 'xingyezhi'
# encoding: utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        temp=addhead=ListNode(0)
        addhead.next=head
        counts=1
        while counts<m:
            temp=temp.next
            counts+=1
        first=temp
        second=temp=temp.next
        while counts<=n:
            temp.next,second.next=first.next,temp.next
            first.next=temp
            temp=second.next
            counts+=1
        self.printList(addhead.next)
        return addhead.next


    def getList(self,l):
        temp=head=ListNode(l[0])
        for i in l[1:]:
            n=ListNode(i)
            temp.next=n
            temp=temp.next
        return head
    def printList(self,head):
        print head.val,
        temp=head.next
        while temp!=None:
            print temp.val,
            temp=temp.next

sol=Solution()
head=sol.getList([1,2,3,4,5])
sol.reverseBetween(head,2,5)