# coding=utf-8
__author__ = 'lenovo'
class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        self.swap(nums,0,len(nums)-k-1)
        self.swap(nums,len(nums)-k,len(nums)-1)
        self.swap(nums,0,len(nums)-1)
    def swap(self,nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

sol=Solution()
sol.rotate([1,2,3,4,5,6,7],3)