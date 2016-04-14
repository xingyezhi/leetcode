__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def trailingZeroes(self, n):
        result=0
        while n!=0:
            result+=n/5
            n/=5
        return result



print '*'*20
sol=Solution()
print sol.trailingZeroes(25)