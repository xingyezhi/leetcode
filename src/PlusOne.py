__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def plusOne(self, digits):
        temp=1
        result=[]
        for i in digits[::-1]:
            result.append((temp+i)%10)
            temp=(temp+i)/10
        if temp!=0:result.append(temp)
        return result[::-1]

sol=Solution()
print sol.plusOne([1,2,3,4,9])