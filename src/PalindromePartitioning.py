__author__ = 'xingyezhi'
# encoding: utf-8

class Solution(object):
    def isPalindrome(self,s):
        l=len(s)
        for i in range(l):
            if s[i]!=s[l-1-i]:
                return False
        else:
            return True
    def partition(self, s):
        self.map={}
        return self.partition2(s[::-1])
    def partition2(self,s):
        if self.map.has_key(s):return self.map[s]
        if len(s)==0:return [[]]
        result=[]
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                temp=self.partition2(s[i+1:])
                for sub in temp:
                    t=sub[:]
                    t.append(s[:i+1])
                    result.append(t)
        self.map[s]=result
        return result
sol=Solution()

print sol.partition("aab")
print sol.map




