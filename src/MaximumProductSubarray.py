# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def maxProduct(self, nums):
        filters=[]
        i=0
        while i<len(nums):
            if nums[i]<0:
                filters.append(nums[i])
                i+=1
            else:
                temp=1
                while i<len(nums) and nums[i]>0:
                    temp*=nums[i]
                    i+=1
                filters.append(temp)
        dp=[0]*len(filters)
        dp[0]=filters[0]
        if len(filters)==1:return dp[0]
        dp[1]=max(filters[1],filters[1]*dp[0])
        result=max(dp[0],dp[1])
        for i in range(2,len(filters)):
            if filters[i]>=0:
                if dp[i-1]>0:dp[i]=dp[i-1]*filters[i]
                else:dp[i]=filters[i]
            else:
                if filters[i-1]<0:
                    dp[i]=max(dp[i-2],1)*filters[i-1]*filters[i]
                else:
                    dp[i]=max(dp[i-3],1)*filters[i-2]*filters[i-1]*filters[i]
            result=max(result,dp[i])
        print filters
        return result

sol=Solution()
print sol.maxProduct([9,2,-1,-7,3,5,-6])

