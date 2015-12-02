__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        strs=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        parsers=[]
        for i in digits:
            j=int(i)
            if j<2:
                continue
            parsers.append(strs[j-2])
        return self.getResult(parsers,0)

    def getResult(self,parsers,now):
        if now==len(parsers)-1:
            return [i for i in parsers[now]]
        nexts=self.getResult(parsers,now+1)
        result=[]
        for i in parsers[now]:
            for j in nexts:
                result.append(i+j)
        return result


sol=Solution()
print sol.letterCombinations("")