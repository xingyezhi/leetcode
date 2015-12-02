__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        maxlength=1
        result=s[0]
        for i in range(len(s)):
            sublength=min(i,len(s)-i-1)
            for j in range(i-1,i-sublength-1,-1):
                t=2*i-j
                if s[j]!=s[t]:
                    break
                elif t-j+1>maxlength:
                    maxlength=t-j+1
                    result=s[j:t+1]

            if i!=0 and s[i]==s[i-1]:
                if maxlength<2:
                    maxlength=2
                    result=s[i-1:i+1]
                sublength=min(i-1,len(s)-1-i)
                for j in range(i-2,i-sublength-2,-1):
                    t=2*i-1-j
                    if s[j]!=s[t]:
                        break
                    elif t-j+1>maxlength:
                        result=s[j:t+1]
                        maxlength=t-j+1
        return result


# sol=Solution()
# print sol.longestPalindrome("a")
# for i in range(10,-1,-1):
#     print i

print 5//2