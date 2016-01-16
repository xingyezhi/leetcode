__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def maxSubArray(self,list):
        middle=0
        result=-10000000
        for i in range(len(list)):
            middle+=list[i]
            result=max(result,middle)
            if middle<0:
                start=i+1
                middle=0
        return result
    def maxSubArray2(self,list):
        if len(list)==1:return list[0]
        middle=len(list)/2
        left=self.maxSubArray2(list[:middle])
        right=self.maxSubArray2(list[middle:])
        temp,l=-1000000,0
        for i in range(middle-1,-1,-1):
            l+=list[i]
            temp=max(temp,l)
        temp2,r=-1000000,0
        for j in range(middle,len(list)):
            r+=list[j]
            temp2=max(temp2,r)
        return max(left,right,temp+temp2)

sol=Solution()
print sol.maxSubArray2([-1,3,2,-2,1,4])