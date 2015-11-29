__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def peru(self,l,k):
        result=[]
        if k==0:return [[]]
        for i in range(len(l)-k+1):
            middle=self.peru(l[i+1:],k-1)
            for j in middle:
                j.append(l[i])
                result.append(j)
        return result
    def combine(self, n, k):
        l=range(1,n+1)
        return [ w[::-1] for w in self.peru(l,k)]


sol=Solution()
print sol.combine(5,3)
# middle=[[1,2],[3,4],[6]]
# [temp.append(0) for temp in middle]
# print middle