__author__ = 'lenovo'
# coding=utf-8

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        maxlength=begin=end=0
        subStr={}
        for i in range(len(s)):
            if not subStr.has_key(s[i]):
                subStr[s[i]]=i
                end=i+1
                maxlength=max(maxlength,end-begin)
            else:
                temp=subStr[s[i]]
                for j in range(begin,temp+1):
                    subStr.pop(s[j])
                subStr[s[i]]=i
                begin=temp+1
                end=i+1
                maxlength=max(maxlength,end-begin)

        return maxlength

sol=Solution()
print sol.lengthOfLongestSubstring("abcabcbb")