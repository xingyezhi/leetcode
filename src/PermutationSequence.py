__author__ = 'lenovo'
# coding=utf-8


class Solution(object):
    def jiecheng(self,n):
        result=1
        for i in range(2,n+1):
            result*=i
        return result
    def getPermutation(self, n, k):
        lenList=[self.jiecheng(i) for i in range(n-1,0,-1)]
        result=[]
        k-=1
        orignal=[str (i) for i in range(1,n+1)]
        for i in range(len(lenList)):
            t=k/lenList[i]
            k%=lenList[i]
            result.append(orignal[t])
            orignal.remove(orignal[t])
        result.extend(orignal)
        print result
        return ''.join(result)



# sol=Solution()
# print ''.join([2,3,4,5])
#print sol.getPermutation(4,1)
t=[1,2,3,4]
print type(str(t)[1])