__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def majorityElement(self, nums):
        cur,result=1,nums[0]
        for i in range(1,len(nums)):
            if cur==0:
                cur,result=1,nums[i]
            elif nums[i]==result:
                cur+=1
            else:
                cur-=1
        return result