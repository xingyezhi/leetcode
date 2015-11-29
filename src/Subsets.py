__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def getResult(self,nums,num):
        result=[]
        for i in range(len(nums)):
            if 1&(num>>i):
                result.append(nums[i])
        return result
    def subsets(self, nums):
        l=range(1,nums+1)
        sum=1<<nums
        result=[]
        for i in range(sum):
            result.append(self.getResult(l,i))
        return result

sol=Solution()
print sol.subsets(3)