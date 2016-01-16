__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        map={}
        result=[]
        for i in nums:
            map.setdefault(i,0)
            map[i]+=1
        alist=sorted(map.iteritems(),key=lambda num:num[0])
        map2={}
        for i in range(len(alist)):
            map2[alist[i][0]]=i
        for i in range(len(alist)):
            arr1=alist[i]
            if arr1[1]>=2:
                keys=-arr1[0]*2
                if map2.has_key(keys) and map2[keys]<i:
                    continue
                if arr1[0]!=keys and map.has_key(-arr1[0]*2):
                    result.append([arr1[0],arr1[0],-arr1[0]*2])
                elif arr1[0]==keys and map[arr1[0]]>=3:
                    result.append([keys,keys,keys])

            for j in range(i+1,len(alist)):
                arr2=alist[j]
                keys=-arr1[0]-arr2[0]
                if map2.has_key(keys) and map2[keys]<j:
                    continue
                if arr2[0]!=keys and map.has_key(keys):
                    result.append([arr1[0],arr2[0],keys])
                elif arr2[0]==keys and map[keys]>=2:
                    result.append([arr1[0],keys,keys])
        return result


sol=Solution()
print sol.threeSum([0,0])