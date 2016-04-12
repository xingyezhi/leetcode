__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def singleNumber(self, nums):
        one=two=three=0
        for i in nums:
            two|=(one&i)
            one^=i
            temp=one&two
            one&=~temp
            two&=~temp
        return one
    def singleNumber2(self, nums):
        a=b=c=0
        for i in nums:
            a2,b2,c2=a,b,c
            a=(a2&~c2&~i)+(i&~c2&~a2)
            b=(b2&~c2&~i)+(a2&i&~b2)+(b2&~a2&i)
            c=(c2&~i)+(~c2&a2&b2&i)
        return c
sol=Solution()
print sol.singleNumber2([2,3,4,2,3,4,2,3,15,15,15,15,4,2,3,4,2,3,4,5,5,5,5,5,6,6,9,9,9,6,6,6,9,9])