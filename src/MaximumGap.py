# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:return 0
        elif len(nums)==2:return abs(nums[1]-nums[0])
        minvalue,maxvalue=min(nums),max(nums)
        if maxvalue==minvalue:return 0
        import math
        gap=int(math.ceil(((float)(maxvalue-minvalue))/(len(nums)-1)))
        #gap+=3
        left,right=[(1<<32)]*len(nums),[-(1<<32)]*len(nums)
        for i in nums:
            index=(i-minvalue)/gap
            left[index]=min(i,left[index])
            right[index]=max(i,right[index])
        result=0
        pre=right[0]
        for i in range(1,len(nums)):
            if left[i]==(1<<32):
                continue
            result=max(result,left[i]-pre)
            pre=right[i]
        return result

sol=Solution()
print sol.maximumGap([1,3,4])