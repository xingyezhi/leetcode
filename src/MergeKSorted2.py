__author__ = 'lenovo'
# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def generateList(self,lists):
        l1=head=ListNode(0)
        for i in lists:
            node=ListNode(i)
            head.next=node
            head=head.next
        return l1.next
    def getData(self,data):
        result=[]
        for l in data:
            head=self.generateList(l)
            result.append(head)
        return result
    def makeHeap(self,heap):
        end=len(heap)-1
        e=(end-1)/2
        for i in range(e,-1,-1):
            temp=i
            l1=temp*2+1
            while l1<len(heap):
                if l1+1<len(heap) and heap[l1].val<heap[l1+1].val:
                    minindex=l1
                elif l1+1<len(heap):
                    minindex=l1+1
                else:
                    minindex=l1
                if heap[temp].val<heap[minindex].val:
                    break
                else:
                    heap[temp],heap[minindex]=heap[minindex],heap[temp]
                    temp=minindex
                    l1=temp*2+1
    def parsers(self,heap):
        temp=0
        l1=temp*2+1
        while l1<len(heap):
            if l1+1<len(heap) and heap[l1].val<heap[l1+1].val:
                minindex=l1
            elif l1+1<len(heap):
                minindex=l1+1
            else:
                minindex=l1
            if heap[temp].val<heap[minindex].val:
                break
            else:
                heap[temp],heap[minindex]=heap[minindex],heap[temp]
                temp=minindex
                l1=temp*2+1
    def mergeKLists(self, lists):
        if len(lists)==0:
            return lists
        elif len(lists)==1:
            return lists[-1]
        heap=[i for i in lists if i!=None]
        self.makeHeap(heap)
        l=head=ListNode(0)
        while len(heap)>=1:
            head.next=heap[0]
            head=head.next
            if heap[0].next!=None:
                heap[0]=heap[0].next
            else:
                heap[0]=heap.pop()
            self.parsers(heap)
        if len(heap)==1:
            head.next=heap[0]
        return l.next

sol=Solution()
data=sol.getData([[],[]])
print sol.mergeKLists(data).val
