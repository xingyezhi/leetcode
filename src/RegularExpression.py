__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def match(self,a,b):
        return 1 if b=='.' or a==b else 0

    def isMatch(self, s, p):
        map=[[0 for i in range(len(p)+1)] for j in range(len(s)+1)]
        map[0][0]=1
        for i in range(0,len(p)):
            if p[i]=='*' and map[0][i-1]:
                map[0][i+1]=1
        for i in range(0,len(s)):
            for j in range(0,len(p)):
                if p[j]=='*':
                    if map[i+1][j-1] or map[i+1][j]:
                        map[i+1][j+1]=1
                    if map[i][j+1] and self.match(s[i],p[j-1]):
                        map[i+1][j+1]=1
                elif map[i][j] and self.match(s[i],p[j]):
                    map[i+1][j+1]=1
        print map
        return map[len(s)][len(p)]!=0




sol=Solution()
print sol.isMatch("aaa", ".*")
# print sol.isMatch("aa","aa")
# print sol.isMatch("aaa","aa")
# print sol.isMatch("aa", "a*")
# print sol.isMatch("aa", ".*")
# print sol.isMatch("ab", ".*")
# print sol.isMatch("aab", "c*a*b")