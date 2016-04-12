# coding=utf-8
__author__ = 'lenovo'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
        l1,cur=0,headA
        while cur!=None:
            l1+=1
            cur=cur.next
        l2,cur=1,headB.next
        pre=headB
        while cur!=None:
            l2+=1
            temp=cur.next
            cur.next=pre
            pre,cur=cur,temp
        cur=headA
        c=1
        while cur!=None and cur!=headB:
            cur=cur.next
            c+=1
        if cur!=headB:
            headB.next=None
            while pre!=None:
                temp=pre.next
                pre.next=cur
                pre,cur=temp,pre
            return None
        ans=(l1+c-l2)/2
        cur,pre=pre,pre.next
        cur.next=None
        headB.next=None
        while pre!=None:
            temp=pre.next
            pre.next=cur
            pre,cur=temp,pre
        result,counts=headA,0
        while counts<ans:
            result=result.next
            counts+=1
        self.printList(headB)
        return result

    def printList(self,head):
        while head!=None:
            print head.val,
            head=head.next
        print
sol=Solution()
headA=ListNode(1)
cur=headA
result=None
for i in range(2,8):
    t=ListNode(i)
    if i==5:
        result=t
    cur.next=t
    cur=t
headB=headA
# b2=ListNode(2)
# headB.next=b2
# b2.next=result
print sol.getIntersectionNode(headA,headB).val