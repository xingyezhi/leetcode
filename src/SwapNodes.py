__author__ = 'lenovo'
# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head==None:
            return None
        elif head.next==None:
            return head
        result=head.next
        l1=result.next
        result.next=head
        l3=head
        while l1!=None:
            l2=l1.next
            if l2==None:
                l3.next=l1
                l3=l1
                break
            temp=l2.next
            l2.next=l1
            l3.next=l2
            l3=l1
            l1=temp
        l3.next=None
        return result

    def printList(self,node):
        while node!=None:
            print node.val,
            node=node.next
        print
    def generateList(self,lists):
        l1=head=ListNode(0)
        for i in lists:
            node=ListNode(i)
            head.next=node
            head=head.next
        return l1.next

sol=Solution()
data=sol.generateList([1,2,3])
sol.printList(sol.swapPairs(data))