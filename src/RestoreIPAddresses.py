__author__ = 'xingyezhi'
# encoding: utf-8
class Solution(object):
    def isValid(self,s):
        t=int(s)
        if t<0 or t>255:
            return False
        return str(t)==s
    def getResult(self,cur,res):
        if len(res)==3:
            if self.isValid(self.s[cur:]):
                res.append(self.s[cur:])
                return [res]
            else:
                return []
        result=[]
        for i in range(cur,len(self.s)-1):
            if self.isValid(self.s[cur:i+1]):
                res.append(self.s[cur:i+1])
                temp=self.getResult(i+1,res[:])
                if len(temp)!=0:
                    result.extend(temp)
                res.pop()
            else:
                break
        return result
    def restoreIpAddresses(self, s):
        if len(s)==0:return []
        self.s=s
        result=self.getResult(0,[])
        result=['.'.join(i) for i in result]
        return result

sol=Solution()
print sol.restoreIpAddresses("010010")
