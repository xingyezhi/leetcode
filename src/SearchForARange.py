__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left=self.getLefter(nums,target)
        if left==-1 or left>=len(nums) or nums[left]!=target:
            return [-1,-1]
        else:
            return[left,self.getRighter(nums,target)-1]
    def getLefter(self,nums,target):
        left=0
        right=len(nums)
        while left<right:
            middle=(left+right)/2
            if nums[middle]>=target:
                right=middle
            else:
                left=middle+1
        return left
    def getRighter(self,nums,target):
        left=0
        right=len(nums)
        while left<right:
            middle=left+(right-left)/2
            if nums[middle]<=target:
                left=middle+1
            else:
                right=middle
        return left

sol=Solution()
print sol.searchRange([2,2], 3)