__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        maxLength=0
        result=""
        if len(strs)==1:
            return strs[0]
        elif len(strs)==0:
            return ""
        for i in range(min(len(strs[0]),len(strs[1]))):
            if strs[0][i]==strs[1][i]:
                maxLength+=1
                result=strs[0][:maxLength]
            else:
                break
        for i in range(2,len(strs)):
            maxLength=min(len(strs[i]),maxLength)
            result=result[:maxLength]
            for j in range(maxLength):
                if result[j]!=strs[i][j]:
                    maxLength=j
                    result=result[:maxLength]
                    break
        return result

sol=Solution()
print sol.longestCommonPrefix(["a","a","b"])

