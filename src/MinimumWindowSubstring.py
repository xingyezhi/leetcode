__author__ = 'lenovo'
# coding=utf-8

class Solution(object):
    def minWindow(self, s, t):
        dictMap,currentMap,counts,start={},{},0,0
        result,get=s,False
        for i in t:
            dictMap.setdefault(i,0)
            dictMap[i]+=1
        for i in range(len(s)):
            if dictMap.has_key(s[i]):
                start,counts=i,1
                currentMap[s[i]]=1
                break
        else:
            return ""
        if len(t)==1:return t
        for j in range(start+1,len(s)):
            if not dictMap.has_key(s[j]):
                continue
            currentMap.setdefault(s[j],0)
            if currentMap[s[j]]<dictMap[s[j]]:
                counts+=1
                currentMap[s[j]]+=1
                if counts==len(t):
                    temp=s[start:j+1]
                    result=temp if len(temp)<len(result) else result
                    get=True
            else:
                currentMap[s[j]]+=1
                while start<=j and ((not dictMap.has_key(s[start])) or currentMap[s[start]]>dictMap[s[start]]):
                    if dictMap.has_key(s[start]):currentMap[s[start]]-=1
                    start+=1
                if counts==len(t):
                    temp=s[start:j+1]
                    result=temp if len(temp)<len(result) else result
        return "" if not get else result



# sol=Solution()
# print sol.minWindow("ab","")
# for i,j in enumerate('abc',4):
#     print i,j

from collections import Counter

t=Counter('abcde')
print t
t['a']=3
t['f']+=1
print t