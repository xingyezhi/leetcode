# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        res=m
        len=n-m
        rest=0
        for i in range(32):
            if res==0:return 0
            if not (1<<i)&res:
                rest=(rest<<1)+1
                continue
            low=m&(rest)
            if len+low>=(2**i):
                res&=~(1<<i)
            rest=(rest<<1)+1
        return res

sol=Solution()
print sol.rangeBitwiseAnd(6,8)