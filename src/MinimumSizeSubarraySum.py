# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def minSubArrayLen(self, s, nums):
        start=sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums>=s:
                break
        else:
            return 0
        result=i-start+1
        j=i
        for j in range(i+1,len(nums)):
            sums+=nums[j]
            while sums>=s:
                result=min(result,j-start+1)
                sums-=nums[start]
                start+=1
        while sums>=s:
            result=min(result,j-start+1)
            sums-=nums[start]
            start+=1
        return result

sol=Solution()
print sol.minSubArrayLen(11,[1,2,3,4,5])