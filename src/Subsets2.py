__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


    def getResult(self,nums,num):
        result=[]
        for i in range(len(nums)):
            if 1&(num>>i):
                result.append(nums[i])
        return result
    def subsets(self, nums):
        nums.sort()
        sum=1<<len(nums)
        result=[]
        for i in range(sum):
            result.append(self.getResult(nums,i))
        return result