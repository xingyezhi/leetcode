__author__ = 'lenovo'
# coding=utf-8
class Solution(object):
    def __init__(self):
        self.result=[]
    def midper(self,nums,cur):
        if cur==len(nums)-1:
            self.result.append(nums[:])
            return
        else:
            for i in range(cur,len(nums)):
                if i!=cur and nums[i]==nums[cur]:
                    continue
                nums[cur],nums[i]=nums[i],nums[cur]
                self.midper(nums[:],cur+1)
    def permuteUnique(self, nums):
        nums.sort()
        self.midper(nums,0)
        return self.result
sol=Solution()
print sol.permuteUnique([1,2,3,4])

# 1 2 3 4
