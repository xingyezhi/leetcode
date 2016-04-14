# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def rob(self, nums):
        dp=[0 for i in range(len(nums)+1)]
        if len(nums)==0:return 0
        elif len(nums)<3:return max(nums)
        dp[1],dp[2]=nums[0],nums[1]
        for i in range(3,len(nums)+1):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i-1]
        return max(dp)


