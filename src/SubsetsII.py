__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def subsetsWithDup(self, nums):
        result,i=[],0
        while i<len(nums):
            same=[nums[i]]
            i+=1
            while i<len(nums) and nums[i]==same[0]:
                same.append(nums[i]);i+=1
            arr=[]
            for j in result:
                for k in range(len(same)):
                    temp=j[:]
                    temp.extend(same[:k+1])
                    arr.append(temp)
            for k in range(len(same)):
               arr.append(same[:k+1])
            result.extend(arr)
        result.append([])
        return result

sol=Solution()
print sol.subsetsWithDup([1,2,2])

#1 1 2
#