# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def findMin(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=low+(high-low)/2
            print nums[mid]
            if nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid
            else:
                high-=1
        return nums[low]

sol=Solution()
print sol.findMin([3,1,3])
