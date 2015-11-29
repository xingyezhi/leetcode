__author__ = 'xingyezhi'
# encoding: utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if len(nums)==0:
            return -1
        left,right=0,len(nums)-1
        middle=left+(right-left)/2
        if nums[middle]==target:
            return middle
        if nums[middle]>=nums[left] and nums[middle]>nums[right]:
            if nums[middle]>target:
                l1=self.binsearch(nums[:middle],target)
                if l1!=-1 and nums[l1]==target:
                    return l1
                else:
                    ans=self.search(nums[middle+1:],target)
                    return ans if ans==-1 else ans+middle+1
            else:
                ans=self.search(nums[middle+1:],target)
                return ans if ans==-1 else ans+middle+1
        elif nums[middle]<nums[left] and nums[middle]<=nums[right]:
                if nums[middle]<target:
                    l1=self.binsearch(nums[middle+1:],target)
                    if nums[middle+1+l1]==target:
                        return middle+1+l1
                    else:
                        return self.search(nums[:middle],target)
                else:
                    return self.search(nums[:middle],target)
        else:
            ans=self.search(nums[:middle],target)
            if ans!=-1:return ans
            ans=self.search(nums[middle+1:],target)
            return middle+1+ans if ans!=-1 else ans
    def binsearch(self,nums,target):
        left=0
        right=len(nums)
        while left<right:
            middle=left+(right-left)/2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            else:
                right=middle
        if left<0:
            return left+1
        elif left>=len(nums):
            return left-1
        else:
            return left

sol=Solution()
print sol.search([3,1],1)

