# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def findKthLargest(self, nums, k):
        return self.findK(nums,len(nums)-k+1,0,len(nums)-1)
    def findK(self,nums,ird,l,r):
        large=self.quickSort(nums,l,r)
        if large+1==ird:return nums[large]
        elif large+1>ird:return self.findK(nums,ird,l,large-1)
        else:return self.findK(nums,ird,large+1,r)
    def quickSort(self,nums,l,r):
        mid=nums[l]
        temp,lcur,rcur=l,l,r
        while lcur<rcur:
            while rcur>lcur and nums[rcur]>=mid:
                rcur-=1
            if rcur>lcur:
                nums[lcur]=nums[rcur]
            while lcur<rcur and nums[lcur]<mid:
                lcur+=1
            if rcur>lcur:
                nums[rcur]=nums[lcur]
        nums[lcur]=mid
        return lcur

sol=Solution()
#print sol.quickSort([2],0,0)
t=[6,2,7,3,8,9]
t=[1]
print sol.findKthLargest(t,1)
