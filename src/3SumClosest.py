__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        result=0
        diff=100000
        if len(nums)<3:
            return ""
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                sums=nums[i]+nums[l]+nums[r]
                if sums==target:
                    return sums
                elif abs(sums-target)<diff:
                    diff=abs(sums-target)
                    result=sums
                if sums<target:
                    l+=1
                else:
                    r-=1
        return result

sol=Solution()
print sol.threeSumClosest([-1,2,1,-4],1)