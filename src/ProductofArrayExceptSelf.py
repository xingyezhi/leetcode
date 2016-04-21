# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def productExceptSelf(self, nums):
        result=[1]*len(nums)
        result[-1]=1
        for i in range(len(nums)-2,-1,-1):
            result[i]=result[i+1]*nums[i+1]
        cur=1
        for i in range(len(nums)):
            result[i]=result[i]*cur
            cur*=nums[i]
        return result
sol=Solution()
sol.productExceptSelf([1,2,3,4])
#[1,2,3,4], return [24,12,8,6]