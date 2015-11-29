__author__ = 'xingyezhi'
# encoding: utf-8



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return str([self.start,self.end])

# [1,6],[8,10],[15,18].
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda inter:(inter.start,inter.end))
        result=[]
        if len(intervals)==0:return result
        start,end=intervals[0].start,intervals[0].end
        for inter in intervals[1:]:
            if inter.start>end:
                result.append(Interval(start,end))
                start,end=inter.start,inter.end
            else:
                end=max(inter.end,end)
        result.append(Interval(start,end))
        return result

    def printList(self,L):
        for key in L:
            print key
sol=Solution()
input=[[1,3],[8,10],[2,6],[15,18]]
L=[]
for key in input:
    i=Interval(key[0],key[1])
    L.append(i)

sol.merge(L)