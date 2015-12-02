__author__ = 'lenovo'
# coding=utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#1  2  3  4  5
class Solution(object):
    def getList(self,l):
        head=t=ListNode(l[0])
        for i in l[1:]:
            temp=ListNode(i)
            t.next=temp
            t=temp
        temp.next=None
        return head
    def printList(self,head):
        result=[]
        temp=head
        while(temp!=None):
            result.append(temp.val)
            temp=temp.next
        print result
    def rotateRight(self, head, k):
        forward=toward=head
        r=ListNode(0)
        if k==0 or toward==None:
            return head
        isend=False
        for i in xrange(k-1):
            if toward.next==None:
                break
            toward=toward.next
        else:
            isend=True
        if not isend :
            return head
        while(toward.next!=None):
            toward=toward.next
            r=forward
            forward=forward.next
        print r.val,forward.val,toward.val
        toward.next=head
        r.next=None
        return forward
sol=Solution()
par1=sol.getList([1,2,3,4,5])
result=sol.rotateRight(par1,5)
sol.printList(result)