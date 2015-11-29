__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def simplifyPath(self, path):
        strlist=path.split('/')
        result=[]
        #print strlist
        for i in strlist:
            if i=='..' and len(result)>0:result.pop()
            elif i in ['.','..','']:continue
            else:result.append(i)
        return '/'+'/'.join(result)

# sol=Solution()
# sol.simplifyPath("/../")
for _ in range(4):
    print _