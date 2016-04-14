__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map={}
        for i in range(len(nums)):
            if nums[i] in map and (i-map[nums[i]])<=k:
                return True
            map[nums[i]]=i
        return False