# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def findPeakElement(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=low+(high-low)/2
            if mid!=0 and nums[mid]<=nums[mid-1]:
                high=mid-1
            elif mid!=(len(nums)-1) and nums[mid]<=nums[mid+1]:
                low=mid+1
            else:
                return mid
        return low

sol=Solution()
print sol.findPeakElement([2])

