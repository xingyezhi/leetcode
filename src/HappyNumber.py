# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def isHappy(self, n):
        map={n:1}
        while n!=1:
            sumsquare=0
            while n!=0:
                sumsquare+=(n%10)**2
                n/=10
            n=sumsquare
            if n in map:
                break
            map[n]=1
        return n==1

sol=Solution()
print sol.isHappy(20)