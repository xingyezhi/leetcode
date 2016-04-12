__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head==None:return head
        counts=0
        result=RandomListNode(0)
        olist=[]
        cur=result.next=head
        nodelist=[result]
        while cur!=None:
            nodelist.append(RandomListNode(cur.label))
            olist.append(cur.label)
            counts+=1
            nodelist[counts-1].next=nodelist[counts]
            cur.label=counts
            cur=cur.next
        cur,cur2=head,nodelist[1]
        icounts=0
        while cur!=None:
            p=cur.random
            if p!=None:
                pcount=p.label
                cur2.random=nodelist[pcount]
            cur.label=olist[icounts]
            icounts+=1
            cur=cur.next
            cur2=cur2.next
        return nodelist[0].next




head=RandomListNode(1)
second=RandomListNode(2)
third=RandomListNode(3)
four=RandomListNode(4)
head.next=second
second.next=third
third.next=four
head.random=third
second.random=head
four.random=second
sol=Solution()
sol.copyRandomList(head)