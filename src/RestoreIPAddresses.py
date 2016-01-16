<<<<<<< HEAD
__author__ = 'xingyezhi'
# encoding: utf-8
=======
__author__ = 'lenovo'
# coding=utf-8

>>>>>>> origin/master
class Solution(object):
    def isValid(self,s):
        t=int(s)
        if t<0 or t>255:
            return False
        return str(t)==s
<<<<<<< HEAD
    def getResult(self,cur,res):
        if len(res)==3:
            if self.isValid(self.s[cur:]):
                res.append(self.s[cur:])
                return [res]
=======
    def getResult(self,cur,counts):
        if self.map.has_key((cur,counts)):
            return self.map[(cur,counts)]
        if counts==3:
            if self.isValid(self.s[cur:]):
                return [[self.s[cur:]]]
>>>>>>> origin/master
            else:
                return []
        result=[]
        for i in range(cur,len(self.s)-1):
            if self.isValid(self.s[cur:i+1]):
<<<<<<< HEAD
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
=======
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
>>>>>>> origin/master
