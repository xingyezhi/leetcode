__author__ = 'xingyezhi'
# encoding: utf-8


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        result=[]
        map={}
        if len(s)<11:return result
        map[s[:10]]=1
        for i in range(11,len(s)):
            map.setdefault(s[i-10:i],0)
            map[s[i-10:i]]+=1
        for i in map:
            if map[i]>1:
                result.append(i)
        print map
        return result

sol=Solution()
print sol.findRepeatedDnaSequences("AAAAAAAAAAA")