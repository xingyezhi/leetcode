__author__ = 'lenovo'
# coding=utf-8
class Solution(object):
    def firstMissingPositive(self, nums):
        if len(nums)==0:
            return 1
        for i in range(len(nums)):
            if nums[i]==i+1 or nums[i]<1 or nums[i]>len(nums):
                continue
            else:
                j=i
                value=nums[j]
                while value>0 and value<len(nums) and value!=j+1:
                    if nums[value-1]==value:
                        break
                    nums[j],nums[value-1]=nums[value-1],nums[j]
                    value=nums[j]
#        print nums
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        else:
            return len(nums)+1



sol=Solution()
print sol.firstMissingPositive([3,1])
