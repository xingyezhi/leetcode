# coding=utf-8
__author__ = 'lenovo'
class Solution(object):
    def rob(self, nums):
        a=self.subrob(nums[1:])
        b=self.subrob(nums[:-1])
        return max(a,b)
    def subrob(self,nums):
        if len(nums)<3:
            return max(nums)
        a,b=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=b
            b=max(a+nums[i],b)
            a=temp
        return b