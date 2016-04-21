# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def singleNumber(self, nums):
        diff=0
        for i in nums:diff^=i
        diff&=(-diff)
        a=b=0
        for i in nums:
            if i&diff:
                a=a^i
            else:b=b^i
        return [a,b]

sol=Solution()
#print [2,3][1]
print sol.singleNumber([2,1,2,3,4,1])