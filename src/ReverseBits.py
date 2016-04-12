# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def reverseBits(self, n):
        t,v=0,n
        for i in range(31):
            t|=(v&1)
            t=(t<<1)
            v=(v>>1)
        t|=(v&1)
        return t
sol=Solution()
print sol.reverseBits(43261596)