# coding=utf-8
__author__ = 'lenovo'

class Solution(object):
    def getResult(self,s,result,index):
        if index==0:return [[]]
        rs=[]
        for i in result[index]:
            temp=self.getResult(s,result,i)
            for j in temp:
                j.append(s[i:index])
                rs.append(j)
        return rs
    def wordBreak(self, s, wordDict):
        result=[[] for i in range(len(s)+1)]
        result[0].append(-1)
        for i in range(1,len(s)+1):
            for j in range(i):
                if len(result[j])>0 and s[j:i] in wordDict:
                    result[i].append(j)
        if len(result[-1])>0:
            return [' '.join(i) for i in self.getResult(s,result,len(s))]
        else:return []

sol=Solution()
print sol.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])

# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].