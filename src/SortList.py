__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        cur,length=head,0
        while cur!=None:
            length+=1
            cur=cur.next
        step=1
        addhead=ListNode(-1)
        addhead.next=head
        while step<length:
            cur,tail=addhead.next,addhead
            while cur!=None:
                left,cur=cur,self.split(cur,step)
                if cur==None:
                    tail.next=left
                    self.printList(addhead.next)
                    break
                right,cur=cur,self.split(cur,step)
                tail=self.merge(left,right,tail)
            step*=2
        return addhead.next

    def split(self,head,step):
        counts=1
        while head.next!=None and counts<step:
            counts+=1
            head=head.next
        temp=head.next
        head.next=None
        return temp
    def merge(self,h1,h2,head):
        cur=head
        while h1 and h2:
            if h1.val<h2.val:
                cur.next=h1
                h1=h1.next
                cur=cur.next
            else:
                cur.next=h2
                h2=h2.next
                cur=cur.next
        cur.next=h1 if h1 else h2
        while cur.next!=None:
            cur=cur.next
        self.printList(head.next)
        return cur

    def printList(self,head,counts=10000):
        c=0
        while head!=None and c<counts:
            print head.val,
            c+=1
            head=head.next
        print

sol=Solution()
head=ListNode(3)
cur=head
for i in range(2,4):
    import random
    t=ListNode(random.randint(1,10))
    cur.next=t
    cur=t
sol.printList(head)
t=sol.sortList(head)
sol.printList(t)
