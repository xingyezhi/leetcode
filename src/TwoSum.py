__author__ = 'lenovo'
# coding=utf-8



def twoSum(self, nums, target):
    dict={}
    for i in range(len(nums)):
        if dict.has_key(nums[i]) and not dict.has_key(str(nums[i])+"s"):
            dict[str(nums[i])+"s"]=i+1;
        else:
            dict[nums[i]]=i+1
    for i in range(len(nums)):
        b=target-nums[i]
        if dict.has_key(b):
            if b!=nums[i]:
                return [dict[nums[i]],dict[b]]
            elif dict.has_key(str(nums[i])+"s"):
                return [dict[nums[i]],dict[str(nums[i])+'s']]


print twoSum(None,[0,4,3,0],0)

