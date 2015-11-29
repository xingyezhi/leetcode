__author__ = 'xingyezhi'
# encoding: utf-8

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return str([self.start,self.end])

class Solution(object):
    def insert(self, intervals, newInterval):
        result=[]
        start,end=newInterval.start,newInterval.end
        if len(intervals)==0:
            result.append(newInterval)
            return result
        for i in range(len(intervals)):
            if intervals[i].start>end:
                result.append(Interval(start,end))
                result.extend(intervals[i:])
                return result
            elif intervals[i].end<start:
                result.append(intervals[i])
            else:
                start=min(intervals[i].start,start)
                end=max(intervals[i].end,end)
        result.append(Interval(start,end))
        self.printList(result)
        return result

    def printList(self,L):
        for key in L:
            print key


input=[[1,5]]
L1=[]
for key in input:
    i=Interval(key[0],key[1])
    L1.append(i)
L2=Interval(2,3)
sol=Solution()
sol.insert(L1,L2)
