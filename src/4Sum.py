__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums=sorted(nums)
        result=[]
        if len(nums)<4:
            return []

        for i in range(len(nums)-3):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    sums=nums[i]+nums[j]+nums[l]+nums[r]
                    if sums<target:
                        l+=1
                    elif sums>target:
                        r-=1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<len(nums)-1 and nums[l]==nums[l+1]:
                            l+=1
                        l+=1
                        while r>1 and nums[r]==nums[r-1]:
                            r-=1
                        r-=1
        return result

sol=Solution()
print sol.fourSum([0,0,0,0], 0)