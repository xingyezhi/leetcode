# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def wordTest(self,s,index,wordDict):
        if index==len(s):return True
        if self.map.has_key(s[index:]):
            return self.map[s[index:]]
        for i in range(index,len(s)):
            if s[index:i+1] in wordDict and self.wordTest(s,i+1,wordDict):
                self.map[s[index:]]=True
                return True
        else:
            self.map[s[index:]]=False
            return False
    def wordBreak(self, s, wordDict):
        self.map={}
        if s==None or len(s)==0:return True
        return self.wordTest(s,0,wordDict)

sol=Solution()
print sol.wordBreak("leetcode",["leet", "code"])

# s = "leetcode",
# dict = ["leet", "code"]