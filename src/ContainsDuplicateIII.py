# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets={}
        t+=1
        for i in range(len(nums)):
            if i>k:
                del(buckets[nums[i-k-1]/t])
            m=nums[i]/t
            if m in buckets:return True
            elif m-1 in buckets and nums[i]-buckets[m-1]<=t:return True
            elif m+1 in buckets and buckets[m+1]-nums[i]<=t:return True
            buckets[m]=nums[i]
        return False
