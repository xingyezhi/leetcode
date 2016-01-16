__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def eq(self,a,b):
        if len(a)!=len(b):
            return False
        for i in range(len(a)):
            if b[i]=='?':
                continue
            elif a[i]!=b[i]:
                return False
        else:
            return True
    def Match(self,a,b):
        for i in range(0,len(a)-len(b)+1):
            if self.eq(a[i:i+len(b)],b):
                return True,i+len(b)
        else:
            return False,len(a)

    def isMatch(self, s, p):
        if len(p)==0:
            return len(s)==0
        startindex=p.find('*')
        endindex=p.rfind('*')
        if startindex==-1 and endindex==-1:
            return self.eq(s,p)
        start=p[:startindex]
        end=p[endindex+1:]
        if len(s)<len(start)+len(end):
            return False
        if not (self.eq(s[:len(start)],start) and self.eq(s[len(s)-len(end):],end)):
            return False
        substr=p[startindex+1:endindex].split('*')
        target=s[len(start):len(s)-len(end)]
        for i in substr:
            if i=="":
                continue
            else:
                temp,tempindex=self.Match(target,i)
                if temp:
                    target=target[tempindex:]
                else:
                    return False
        else:
            return True







sol=Solution()
print sol.isMatch("c"
,"*?*")
