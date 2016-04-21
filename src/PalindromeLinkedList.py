# coding=utf-8
__author__ = 'lenovo'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
    # def isPalindrome(self, head):
    #     cur=head
    #     length=0
    #     while cur!=None:
    #         length+=1
    #         cur=cur.next
    #     leftcounts=0
    #     cur,pre=head,None
    #     while leftcounts<length/2:
    #         temp=cur.next
    #         cur.next,pre=pre,cur
    #         cur=temp
    #         leftcounts+=1
    #     left=pre
    #     if length&1:
    #         right=cur.next
    #     else:right=cur
    #     while right!=None:
    #         if right.val!=left.val:return False
    #         right,left=right.next,left.next
    #     while pre!=None:
    #         temp=pre.next
    #         pre.next,cur=cur,pre
    #         pre=temp
    #     return True


# sol=Solution()
# newhead=ListNode(-1)
# value=[0,1,1,0]
# pre=newhead
# for i in value:
#     cur=ListNode(i)
#     pre.next=cur
#     pre=cur
# print sol.isPalindrome(newhead.next)
a1=a=ListNode(1)
b1=b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c
a,a.next,b=b,a,b.next
print a1.val,a1.next.val
print a.val,a.next.val
print b.val,b.next