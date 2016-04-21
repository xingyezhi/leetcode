# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def nthUglyNumber(self, n):
        onecount=[0,0,0]
        result=[1]
        cur=counts=1
        while counts<n:
            temp=map(lambda x,y:x*y,[2,3,5],[result[i] for i in onecount])
            cur=min(temp)
            for i,value in enumerate(temp):
                if value==cur:
                    onecount[i]+=1
            result.append(cur)
            counts+=1
        return cur

sol=Solution()
print sol.nthUglyNumber(11)
# a=[1,2,3]
# b=[2,3,5]
# print map(lambda x,y:x*y,a,b)
# print a