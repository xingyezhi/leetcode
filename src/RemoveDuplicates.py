__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        counts=1
        if len(nums)==0:
            return 0
        nums.append('*')
        i=1
        while nums[i]!='*':
            if nums[i]!=nums[i-1]:
                counts+=1
                i+=1
            else:
                nums.remove(nums[i])

        print nums[:counts]
        return counts
    def removeElement(self, nums, val):
        newlength=0
        if len(nums)==0:
            return 0
        for i in nums:
            if i!=val:
                nums[newlength]=i
                newlength+=1
        print nums[:newlength]
        return newlength

sol=Solution()
print sol.removeElement([2],3)
