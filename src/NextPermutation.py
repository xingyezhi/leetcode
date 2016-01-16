__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def reverse(self,nums,start=0):
        mid=(start+len(nums))/2
        for i in range(start,mid):
            nums[i],nums[start+len(nums)-1-i]=nums[start+len(nums)-1-i],nums[i]
        print nums
    def nextPermutation(self, nums):
        if len(nums)==0:
            return
        i=0
        for j in range(len(nums)-1,0,-1):
            if nums[j]>nums[j-1]:
                i=j
                break
        if i==0:
            self.reverse(nums)
            return
        m=i
        for j in range(len(nums)-1,i-1,-1):
            if nums[j]>nums[i-1]:
                m=j
                break
        print nums[i-1],nums[m]
        nums[i-1],nums[m]=nums[m],nums[i-1]

        self.reverse(nums,i)
sol=Solution()
sol.nextPermutation([3,2,1])