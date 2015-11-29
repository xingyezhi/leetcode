__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)<=2:return len(nums)
        counts=i=0
        while i<len(nums):
            temp=1
            while i+1<len(nums) and nums[i]==nums[i+1]:
                temp+=1;i+=1
            if temp>=2:
                nums[counts]=nums[counts+1]=nums[i]
                counts+=2
            else:
                nums[counts]=nums[i];counts+=1
            i+=1
        print nums
        return counts

sol=Solution()
print sol.removeDuplicates([1,1,1,2,2,3])