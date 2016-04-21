# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def summaryRanges(self, nums):
        rangeresult=self.getRange(0,len(nums)-1,nums)
        return [str(r[0]) if r[0]==r[1] else str(r[0])+"->"+str(r[1]) for r in rangeresult]
    def getRange(self,left,right,nums):
        if right<left:return []
        if right-left==nums[right]-nums[left]:return [(nums[left],nums[right])]
        mid=left+(right-left)/2
        leftresult=self.getRange(left,mid,nums)
        rightresult=self.getRange(mid+1,right,nums)
        if len(leftresult)==0 or len(rightresult)==0:
            return leftresult+rightresult
        else:
            if leftresult[-1][1]==rightresult[0][0]-1:
                return leftresult[:-1]+[(leftresult[-1][0],rightresult[0][1])]+rightresult[1:]
            return leftresult+rightresult


sol=Solution()
print sol.summaryRanges([])