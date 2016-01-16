__author__ = 'lenovo'
# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
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

    def reverseKGroup(self, head, k):
        if head==None or k<=1:
            return head
        nodeList=[]
        top=head
        while head!=None and len(nodeList)<k:
            nodeList.append(head)
            head=head.next
        if len(nodeList)<k:
            return top
        result=nodeList[-1]
        l3=nodeList[0]
        l1=result.next
        for i in range(len(nodeList)-1,0,-1):
            nodeList[i].next=nodeList[i-1]
        while l1!=None:
            counts=0
            begin=l1
            while l1!=None and counts<k:
                nodeList[counts]=l1
                l1=l1.next
                counts+=1
            if counts<k:
                l3.next=begin
                l3=nodeList[counts-1]
                break
            l1=nodeList[-1].next
            l3.next=nodeList[-1]
            for i in range(len(nodeList)-1,0,-1):
               nodeList[i].next=nodeList[i-1]
            l3=nodeList[0]

        l3.next=None
        return result

sol=Solution()
data=sol.generateList([1])
sol.printList(sol.reverseKGroup(data,2))