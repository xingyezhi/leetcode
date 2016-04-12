# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def combinationSum3(self, k, n):
        return self.combination(1,k,n)
    def combination(self,cur,k,n):
        if k==1:
            if cur<=n<10:
                return [[n]]
            else:
                return []
        end=min(n/k+1,8)
        result=[]
        for i in range(cur,end):
            temp=self.combination(i+1,k-1,n-i)
            for j in temp:
                t=[i]
                t.extend(j)
                result.append(t)
        return result

sol=Solution()
print sol.combinationSum3(3,9)