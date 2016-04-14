__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def singleNumber(self, nums):
        result=nums[0]
        for i in nums[1:]:
            result^=i
        return result

sol=Solution()
print sol.singleNumber([2,2,3,3,1,1,5])