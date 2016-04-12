# coding=utf-8
__author__ = 'lenovo'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        counts,cur=0,head
        while cur!=None:
            cur=cur.next
            counts+=1
        if counts<3:return
        mid=counts/2
        cur,i=head,0
        while i<mid:
            cur=cur.next
            i+=1
        tail,p=cur,cur.next
        while p!=None:
            temp=p.next
            p.next=tail
            tail,p=p,temp
        front=head
        cur.next=None
        while front!=tail:
            f2,t2=front.next,tail.next
            if f2==None or t2==None:break
            front.next=tail
            tail.next=f2
            front,tail=f2,t2

    def printList(self,head):
        cur=head
        while cur!=None:
            print cur.val,
            cur=cur.next
        print

sol=Solution()
t=head=ListNode(1)
for i in range(2,5):
    temp=ListNode(i)
    t.next=temp
    t=temp
sol.printList(head)
sol.reorderList(head)
sol.printList(head)



