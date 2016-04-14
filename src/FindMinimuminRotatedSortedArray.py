# coding=utf-8
__author__ = 'lenovo'

#4 5 6 7 0 1 2
class Solution(object):
    def findMin(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=low+(high-low)/2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]

sol=Solution()
print sol.findMin([4,5,6,7,0,1,2])
