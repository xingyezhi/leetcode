__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def sortColors(self, nums):
        if len(nums)==0:return nums
        i,j=0,len(nums)-1
        counts1=counts3=counts2=0
        while i<j:
            while i<j and nums[i]==0:
                nums[counts1]=0;i+=1;counts1+=1
            while i<j and nums[j]==2:
                nums[len(nums)-1-counts3]=2;j-=1;counts3+=1
            if i<j and (nums[i]==2 or nums[j]==0):
                nums[i],nums[j]=nums[j],nums[i]
            elif i<j:
                i+=1;j-=1;counts2+=2
        if i==j:
            if nums[i]==0:nums[counts1]=0;counts1+=1
            elif nums[i]==2:nums[len(nums)-1-counts3]=2;
            else:counts2+=1
        for i in range(counts1,counts1+counts2):
            nums[i]=1
        print nums

sol=Solution()
sol.sortColors([2])