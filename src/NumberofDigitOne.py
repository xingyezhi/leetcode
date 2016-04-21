# coding=utf-8
__author__ = 'lenovo'


class Solution(object):
    def countDigitOne(self, n):
        if n<=0:return 0
        s=str(n)
        length=len(s)-1
        result=0
        for i in range(len(s)-1):
            n%=(10**length)
            cur=int(s[i])
            if cur>1:
                result+=cur*(length*(10**(length-1)))+(10**length)
            elif cur<1:
                result+=cur*(length*(10**(length-1)))
            else:result+=cur*(length*(10**(length-1)))+(n+1)
            length-=1
        result+=1 if int(s[-1])!=0 else 0
        return result

sol=Solution()
print sol.countDigitOne(10)