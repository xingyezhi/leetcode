__author__ = 'lenovo'
# coding=utf-8

class Solution:

    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack=[]
        map={}
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    continue
                else:
                    index=stack.pop()
                    map[index]=i-index+1
        maxlength=0
        print map
        for i in map:
            length=map[i]
            end=i+map[i]
            while map.has_key(end):
                length+=map[end]
                end+=map[end]
            maxlength=max(maxlength,length)

        return maxlength
sol=Solution()
print sol.longestValidParentheses("()()")