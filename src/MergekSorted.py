__author__ = 'lenovo'
# coding=utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def generateList(self,lists):
        l1=head=ListNode(0)
        for i in lists:
            node=ListNode(i)
            head.next=node
            head=head.next
        return l1.next

    def mergeTwoLists(self, l1, l2):
        result=ListNode(0)
        head=result
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
                head=head.next
            else:
                head.next=l2
                l2=l2.next
                head=head.next
        if l1!=None:
            head.next=l1
        else:
            head.next=l2
        return result.next

    def mergeKLists(self, lists):
        if len(lists)==0:
            return lists
        if len(lists)==1:
            return lists[-1]
        size=len(lists)
        newList=[]
        mergelength=size-1 if size&1 else size
        for i in range(mergelength/2):
            newList.append(self.mergeTwoLists(lists[i],lists[mergelength-1-i]))
        if size&1:
            newList.append(lists[-1])
        return self.mergeKLists(newList)

sol=Solution()
