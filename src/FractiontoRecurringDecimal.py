# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        t=1 if numerator*denominator>=0 else -1
        numerator,denominator=abs(numerator),abs(denominator)
        mid=numerator/denominator
        other=numerator%denominator
        mid=`mid` if t>0 else ('-'+`mid`)
        if other==0:return str(mid)
        self.result=[str(mid),'.']
        self.map={}
        self.cur=0
        self.division(other*10,denominator)
        if self.cur==0:
            return ''.join(self.result)
        print self.cur,self.result
        a=''.join(self.result[:self.cur])
        b=''.join(self.result[self.cur:])
        return a+"("+b+")"

    def division(self,a,b):
        if a%b==0:
            self.result.append(str(a/b))
            return
        m,n=a/b,(a%b)*10
        self.result.append(str(m))
        self.map[a]=len(self.result)-1
        if n in self.map:
            self.cur=self.map[n]
            return
        self.division(n,b)



sol=Solution()
print sol.fractionToDecimal(-7,12)
