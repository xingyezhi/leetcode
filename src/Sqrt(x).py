__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    # def mySqrt(self, x):
    #     if x==0:return 0
    #     left,right=1,x/2+1
    #     while left+1<right:
    #         #print left,right
    #         middle=left+(right-left)/2
    #         temp=middle*middle
    #         if temp==x:return middle
    #         elif temp<x:left=middle
    #         else:right=middle
    #     return left
    def mySqrt(self, x):
        if x in [0,1]:return x
        g0,g1=1,(x+1)/2
        print g0,g1
        while g0==1 or g0>g1:
            g0=g1
            g1=(g0+x/g0)/2
            print g0,g1
        return g0


sol=Solution()
print sol.mySqrt(3)