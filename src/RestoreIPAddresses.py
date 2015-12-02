__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def isValid(self,s):
        t=int(s)
        if t<0 or t>255:
            return False
        return str(t)==s
    def getResult(self,cur,counts):
        if self.map.has_key((cur,counts)):
            return self.map[(cur,counts)]
        if counts==3:
            if self.isValid(self.s[cur:]):
                return [[self.s[cur:]]]
            else:
                return []
        result=[]
        for i in range(cur,len(self.s)-1):
            if self.isValid(self.s[cur:i+1]):
                temp=self.getResult(i+1,counts+1)
                temp2=[]
                for j in temp:
                    t=j[:]
                    t.append(self.s[cur:i+1])
                    temp2.append(t)
                if len(temp2)!=0:
                    result.extend(temp2)
            else:
                break
        self.map[(cur,counts)]=result
        return result
    def restoreIpAddresses(self, s):
        self.map={}
        self.s=s
        result=self.getResult(0,0)
        result=['.'.join(i[::-1]) for i in result]
        return result

sol=Solution()
print sol.restoreIpAddresses("101023")