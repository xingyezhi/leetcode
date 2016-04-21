# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:return n
        while n!=1:
            if n&1:
                return False
            n=n>>1
        return True


sol=Solution()
# print sol.isPowerOfTwo(64)
a=11
print a
a=a&(a-1)
print a
a=a&(a-1)
print a