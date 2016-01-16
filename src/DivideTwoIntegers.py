__author__ = 'lenovo'
# coding=utf-8
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def getCounts(self,a,b):
        m,n=a,b
        l1,l2=0,0
        counts=1
        if a<b:
            return 0
        elif a==b:
            return 1
        while n<m:
            l1=n
            n+=n
            l2=counts
            counts+=counts
        if n==m:
            return counts
        else:
            counts-=l2
            n-=l1
            return counts+self.getCounts(a-n,b)
    def divide(self, dividend, divisor):
        if divisor==0:
            return 2147483647
        a=dividend if dividend>0 else -dividend
        b=divisor if divisor>0 else -divisor
        if a<b or a==0:
            return 0
        else:
            counts=self.getCounts(a,b)
            if dividend>0 and  divisor>0:
                return counts if counts<2147483648 else 2147483647
            elif dividend<0 and divisor<0:
               return counts if counts<2147483648 else 2147483647
            else:
                return -counts

sol=Solution()
print sol.divide(-2147483648, -1)