__author__ = 'lenovo'
# coding=utf-8


class Solution(object):
    def myPow(self, x, n):
       if n<0:
           return float(1)/(self.myPow(x,-n))
       elif n==0:
           return 1
       if n==1:
           return x
       if n&1:
           return x*(self.myPow(x,n/2)**2)
       else:
           return self.myPow(x,n/2)**2

def test(x,n):
    result=1
    for i in range(n):
        result=result*x
    return result
sol=Solution()
print sol.myPow(0.00001,2147483647)
print test(0.00001,2147483647)